#!/usr/bin/env python3
"""Cached feed access for OSV, CISA KEV and FIRST EPSS.

Network is off by default. A lookup reads the cache when it is fresh, then the
repository seed. Only ``--online`` refreshes over the network. A failed fetch
falls back to the cache, then the seed, and records the error.

Cache files live in ``data/feed_cache`` and are gitignored. Writes are atomic.
Payloads are capped and time limited.

    python scripts/feeds.py status
    python scripts/feeds.py update --online
    python scripts/feeds.py lookup --cve CVE-2021-44228
    python scripts/feeds.py osv --ecosystem npm --package lodash --version 4.17.20 --online
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fileio
import paths

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = paths.DATA
CACHE = os.path.join(DATA, "feed_cache")
UA = "Beril/1.4 feeds (+https://github.com/sheduxdev/beril)"
TIMEOUT = 20
MAX_BYTES = 40_000_000

SOURCES = {
    "kev": {
        "url": "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json",
        "seed": os.path.join(DATA, "kev.json"),
        "ttl": 24 * 3600,
    },
    "epss": {
        "url": "https://api.first.org/data/v1/epss",
        "seed": os.path.join(DATA, "epss.json"),
        "ttl": 12 * 3600,
    },
    "osv": {
        "url": "https://api.osv.dev/v1/query",
        "seed": os.path.join(DATA, "osv_seed.json"),
        "ttl": 12 * 3600,
    },
}
ERRORS: list[str] = []


def now() -> dt.datetime:
    return dt.datetime.now(dt.UTC)


def stamp() -> str:
    return now().isoformat(timespec="seconds")


def cache_path(name: str, key: str = "") -> str:
    suffix = hashlib.sha256(key.encode()).hexdigest()[:16] if key else "default"
    return os.path.join(CACHE, f"{name}-{suffix}.json")


def read_cache(name: str, key: str = "") -> dict | None:
    data = fileio.load_json(cache_path(name, key), None)
    if not isinstance(data, dict):
        return None
    try:
        fetched = dt.datetime.fromisoformat(data.get("fetched_at", ""))
    except ValueError:
        return None
    if fetched.tzinfo is None:
        fetched = fetched.replace(tzinfo=dt.UTC)
    return data


def fresh(entry: dict | None, ttl: int) -> bool:
    if not entry:
        return False
    try:
        fetched = dt.datetime.fromisoformat(entry.get("fetched_at", ""))
    except ValueError:
        return False
    if fetched.tzinfo is None:
        fetched = fetched.replace(tzinfo=dt.UTC)
    return (now() - fetched).total_seconds() < ttl


def write_cache(name: str, key: str, payload: dict, source: str) -> str:
    path = cache_path(name, key)
    os.makedirs(CACHE, exist_ok=True)
    wrapper = {"fetched_at": stamp(), "source": source, "payload": payload}
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as handle:
        json.dump(wrapper, handle, ensure_ascii=False)
        handle.write("\n")
    os.replace(tmp, path)
    return path


def http_json(url: str, body: dict | None = None) -> dict:
    headers = {"User-Agent": UA, "Accept": "application/json"}
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        raw = response.read(MAX_BYTES)
    return json.loads(raw.decode("utf-8"))


def seed(name: str) -> dict:
    data = fileio.load_json(SOURCES[name]["seed"], {})
    return data if isinstance(data, dict) else {}


def load_kev(online: bool = False, ttl: int | None = None) -> dict:
    """Load KEV, cache first, seed last.

    Args:
        online: Refresh over the network when the cache is stale.
        ttl: Override the freshness window in seconds.

    Returns:
        A payload with a ``cves`` mapping and a ``from`` marker.
    """
    entry = read_cache("kev")
    if entry and fresh(entry, ttl or SOURCES["kev"]["ttl"]):
        return {**entry["payload"], "from": "cache"}
    if online:
        try:
            raw = http_json(SOURCES["kev"]["url"])
            cves = {}
            for item in raw.get("vulnerabilities", []):
                cve = str(item.get("cveID", "")).upper()
                if not cve.startswith("CVE-"):
                    continue
                cves[cve] = {
                    "name": (item.get("vulnerabilityName") or "")[:200],
                    "vendor": (item.get("vendorProject") or "")[:100],
                    "date_added": item.get("dateAdded", ""),
                    "ransomware": item.get("knownRansomwareCampaignUse", ""),
                }
            write_cache("kev", "", {"cves": cves}, SOURCES["kev"]["url"])
            return {"cves": cves, "from": "network"}
        except Exception as exc:
            ERRORS.append(f"kev: {type(exc).__name__}: {exc}")
    if entry:
        return {**entry["payload"], "from": "stale-cache"}
    return {**seed("kev"), "from": "seed"}


def load_epss(cve: str, online: bool = False, ttl: int | None = None) -> dict:
    """Load one EPSS score, cache first, seed last.

    Args:
        cve: CVE id.
        online: Refresh over the network when the cache is stale.
        ttl: Override the freshness window.

    Returns:
        A payload with ``score``, ``percentile`` and a ``from`` marker.
    """
    cve = cve.upper()
    entry = read_cache("epss", cve)
    if entry and fresh(entry, ttl or SOURCES["epss"]["ttl"]):
        return {**entry["payload"], "from": "cache"}
    if online:
        try:
            raw = http_json(f"{SOURCES['epss']['url']}?cve={cve}")
            row = (raw.get("data") or [{}])[0]
            payload = {
                "cve": cve,
                "score": float(row.get("epss", 0) or 0),
                "percentile": float(row.get("percentile", 0) or 0),
            }
            write_cache("epss", cve, payload, SOURCES["epss"]["url"])
            return {**payload, "from": "network"}
        except Exception as exc:
            ERRORS.append(f"epss {cve}: {type(exc).__name__}: {exc}")
    if entry:
        return {**entry["payload"], "from": "stale-cache"}
    score = (seed("epss").get("scores") or {}).get(cve)
    return {"cve": cve, "score": float(score) if score is not None else None, "percentile": None, "from": "seed"}


def load_epss_table(online: bool = False) -> dict:
    """Load the seed table plus fresh single-CVE cache entries."""
    table = {k: v for k, v in (seed("epss").get("scores") or {}).items() if v is not None}
    if os.path.isdir(CACHE):
        for name in os.listdir(CACHE):
            if not name.startswith("epss-"):
                continue
            entry = fileio.load_json(os.path.join(CACHE, name), None)
            if not isinstance(entry, dict):
                continue
            payload = entry.get("payload") or {}
            cve, score = payload.get("cve"), payload.get("score")
            if cve and score is not None:
                table[cve] = score
    if online and not table:
        load_epss("CVE-2021-44228", online=True)
    return table


def osv_query(ecosystem: str, package: str, version: str, online: bool = False, ttl: int | None = None) -> dict:
    """Query OSV for one package version.

    Args:
        ecosystem: OSV ecosystem, e.g. npm or PyPI.
        package: Package name.
        version: Exact version.
        online: Refresh over the network when the cache is stale.
        ttl: Override the freshness window.

    Returns:
        A payload with ``vulns`` and a ``from`` marker.
    """
    key = f"{ecosystem}|{package}|{version}"
    entry = read_cache("osv", key)
    if entry and fresh(entry, ttl or SOURCES["osv"]["ttl"]):
        return {**entry["payload"], "from": "cache"}
    if online:
        try:
            raw = http_json(
                SOURCES["osv"]["url"], {"package": {"name": package, "ecosystem": ecosystem}, "version": version}
            )
            payload = {"ecosystem": ecosystem, "package": package, "version": version, "vulns": raw.get("vulns", [])}
            write_cache("osv", key, payload, SOURCES["osv"]["url"])
            return {**payload, "from": "network"}
        except Exception as exc:
            ERRORS.append(f"osv {package}@{version}: {type(exc).__name__}: {exc}")
    if entry:
        return {**entry["payload"], "from": "stale-cache"}
    seeded = ((seed("osv").get("packages") or {}).get(ecosystem) or {}).get(package) or {}
    vulns = []
    for below, meta in seeded.items():
        if version_lt(version, below.lstrip("<")):
            vulns.append(meta)
    return {"ecosystem": ecosystem, "package": package, "version": version, "vulns": vulns, "from": "seed"}


def osv_query_many(
    items: list[tuple[str, str, str]], online: bool = False, limit: int = 500
) -> tuple[list[list[dict]], list[str], str]:
    """Query OSV for many package versions in one request.

    Fresh cache entries answer first. Only misses go over the wire.

    Args:
        items: ``(ecosystem, package, version)`` tuples.
        online: Allow one network batch for the misses.
        limit: Maximum items sent.

    Returns:
        Vuln lists in input order, errors, and a from marker.
    """
    items = items[:limit]
    results: list[list[dict]] = []
    misses: list[tuple[int, tuple[str, str, str]]] = []
    for index, item in enumerate(items):
        entry = read_cache("osv", "|".join(item))
        if entry and fresh(entry, SOURCES["osv"]["ttl"]):
            results.append(entry["payload"].get("vulns") or [])
        else:
            results.append([])
            misses.append((index, item))
    errors = []
    marker = "cache"
    if misses and online:
        marker = "network"
        body = {
            "queries": [
                {"package": {"name": package, "ecosystem": ecosystem}, "version": version}
                for _index, (ecosystem, package, version) in misses
            ]
        }
        try:
            raw = http_json(SOURCES["osv"]["url"].replace("/query", "/querybatch"), body)
            rows = raw.get("results") or []
            for (index, item), row in zip(misses, rows, strict=False):
                vulns = row.get("vulns") or []
                results[index] = vulns
                write_cache(
                    "osv",
                    "|".join(item),
                    {"ecosystem": item[0], "package": item[1], "version": item[2], "vulns": vulns},
                    SOURCES["osv"]["url"],
                )
        except Exception as exc:
            errors.append(f"osv batch: {type(exc).__name__}: {exc}")
    elif misses:
        marker = "seed"
    return results, errors, marker


def version_lt(value: str, below: str) -> bool:
    def parts(text: str) -> tuple[int, ...]:
        nums = [int(x) for x in re.findall(r"\d+", text)[:4]]
        return tuple(nums) if nums else (0,)

    return parts(value) < parts(below)


def status() -> dict:
    out = {}
    for name in SOURCES:
        entry = read_cache(name)
        path = cache_path(name)
        out[name] = {
            "cache": path if os.path.exists(path) else "",
            "fetched_at": entry.get("fetched_at") if entry else "",
            "fresh": fresh(entry, SOURCES[name]["ttl"]),
            "seed": os.path.exists(SOURCES[name]["seed"]),
        }
    out["errors"] = ERRORS[-10:]
    return out


def update(online: bool = True) -> dict:
    """Refresh the KEV cache.

    EPSS and OSV are per-item, so they refresh on lookup. Seed files stay as
    the last fallback and are not overwritten here.

    Args:
        online: Must be true to touch the network.

    Returns:
        Status counts.
    """
    if not online:
        return {"online": False, "kev": 0, "refreshed_at": stamp()}
    before = time.monotonic()
    data = load_kev(online=True)
    count = len(data.get("cves") or {})
    return {
        "online": True,
        "kev": count,
        "seconds": round(time.monotonic() - before, 2),
        "errors": ERRORS[-5:],
        "refreshed_at": stamp(),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=("status", "update", "lookup", "osv"))
    ap.add_argument("--online", action="store_true")
    ap.add_argument("--cve", default="")
    ap.add_argument("--ecosystem", default="")
    ap.add_argument("--package", default="")
    ap.add_argument("--version", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if args.command == "status":
        result = status()
    elif args.command == "update":
        result = update(args.online)
    elif args.command == "lookup":
        if not args.cve:
            sys.exit("--cve required")
        result = load_epss(args.cve, args.online)
        result["kev"] = args.cve.upper() in (load_kev(args.online).get("cves") or {})
    else:
        if not (args.ecosystem and args.package and args.version):
            sys.exit("--ecosystem, --package and --version required")
        result = osv_query(args.ecosystem, args.package, args.version, args.online)
    print(
        json.dumps(result, indent=2, ensure_ascii=False)
        if args.json
        else "\n".join(f"{k}: {v}" for k, v in result.items())
    )


if __name__ == "__main__":
    main()
