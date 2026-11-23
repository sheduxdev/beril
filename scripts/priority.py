#!/usr/bin/env python3
"""Exploit-priority data: CISA KEV, EPSS and CVSS.

A CVSS number alone does not answer "what do I patch first". KEV says the bug
is exploited in the wild. EPSS says how likely exploitation is in the next 30
days. Both together are better than either alone, and neither replaces the
asset context.

The repository ships a dated seed so the tool works offline. Refresh it with
``--update``. Network access is read-only and fetches public JSON.

    python scripts/priority.py --update
    python scripts/priority.py --cve CVE-2021-44228
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import feeds
import paths

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = paths.DATA
KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
EPSS_URL = "https://api.first.org/data/v1/epss?cve={cve}"
UA = "Beril/1.4 (priority refresh)"

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.I)


def _load(name: str) -> dict:
    path = os.path.join(DATA, name)
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError):
        return {}


def load_kev() -> dict:
    return feeds.load_kev().get("cves", {})


def load_epss() -> dict:
    return feeds.load_epss_table()


def cves_in(text: str) -> list[str]:
    return sorted({m.group(0).upper() for m in CVE_RE.finditer(text or "")})


def enrich(cve: str, kev: dict | None = None, epss: dict | None = None) -> dict:
    cve = cve.upper()
    kev = kev if kev is not None else load_kev()
    epss = epss if epss is not None else load_epss()
    return {
        "cve": cve,
        "kev": cve in kev,
        "kev_name": kev.get(cve, {}).get("name", ""),
        "kev_added": kev.get(cve, {}).get("date_added", ""),
        "epss": epss.get(cve),
    }


def update() -> dict:
    """Refresh KEV and the EPSS scores for the CVEs already in the seed."""
    report = {"kev": 0, "epss": 0, "errors": []}
    result = feeds.update(online=True)
    report["kev"] = result.get("kev", 0)
    report["errors"] += result.get("errors", []) + feeds.ERRORS
    existing = feeds.load_epss_table()
    refreshed = {}
    for cve in list(existing)[:400]:
        row = feeds.load_epss(cve, online=True)
        if row.get("from") == "network" and row.get("score") is not None:
            refreshed[cve] = row["score"]
            report["epss"] += 1
        elif row.get("score") is not None:
            refreshed[cve] = row["score"]
    _write(
        "epss.json",
        {
            "source": feeds.SOURCES["epss"]["url"],
            "updated": dt.date.today().isoformat(),
            "note": "FIRST EPSS snapshot, seed CVEs only",
            "scores": refreshed,
        },
    )
    return report


def _write(name: str, payload: dict) -> None:
    path = os.path.join(DATA, name)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, path)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--update", action="store_true")
    ap.add_argument("--cve", default="")
    args = ap.parse_args()
    if args.update:
        print(json.dumps(update(), indent=2, ensure_ascii=False))
    elif args.cve:
        print(json.dumps(enrich(args.cve), indent=2, ensure_ascii=False))
    else:
        kev, epss = load_kev(), load_epss()
        print(f"KEV entries: {len(kev)}")
        print(f"EPSS entries: {len(epss)}")
        sys.exit(0 if kev else 1)


if __name__ == "__main__":
    main()
