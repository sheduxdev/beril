#!/usr/bin/env python3
"""Ownership verification and scope gate for active checks.

Passive GETs against a public page are one thing. Sending payloads, probing
ports or testing parameters is another. Beril refuses active work until the
target proves control with one of three tokens:

1. DNS TXT record ``_beril.<host>`` containing the token.
2. File ``/.well-known/beril-verify.txt`` containing the token.
3. Meta tag ``<meta name="beril-verify" content="token">`` on the home page.

The record is stored under ``.beril/authorizations/<host>.json`` with an expiry
(30 days by default). A scope file can narrow hosts further. If no verification
exists, ``--owned`` records an explicit human acknowledgement instead.

    python scripts/authz.py --new example.com
    python scripts/authz.py --check example.com
    python scripts/authz.py --verify example.com
"""

from __future__ import annotations

import argparse
import datetime as dt
import hmac
import ipaddress
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

STORE = ".beril/authorizations"
DAYS = 30
UA = "Beril/1.4 ownership-check"


def now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def token() -> str:
    return "beril-" + os.urandom(16).hex()


def _path(host: str) -> str:
    safe = re.sub(r"[^a-z0-9.-]+", "_", host.lower())
    return os.path.join(STORE, safe + ".json")


def record(host: str, method: str, token_value: str, evidence: str, note: str = "") -> dict:
    entry = {
        "host": host.lower(),
        "method": method,
        "token": token_value,
        "evidence": evidence,
        "note": note,
        "verified_at": now().isoformat(timespec="seconds"),
        "expires_at": (now() + dt.timedelta(days=DAYS)).isoformat(timespec="seconds"),
    }
    os.makedirs(STORE, exist_ok=True)
    with open(_path(host), "w", encoding="utf-8") as fh:
        json.dump(entry, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    return entry


def load(host: str) -> dict | None:
    try:
        with open(_path(host), encoding="utf-8") as fh:
            entry = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None
    try:
        expires = dt.datetime.fromisoformat(entry.get("expires_at", ""))
    except ValueError:
        return None
    if expires < now():
        return None
    return entry


def dns_token(host: str) -> str:
    name = f"_beril.{host}"
    if shutil.which("dig"):
        out = subprocess.run(["dig", "+short", "TXT", name], capture_output=True, text=True, timeout=10).stdout
    elif shutil.which("nslookup"):
        out = subprocess.run(["nslookup", "-type=TXT", name], capture_output=True, text=True, timeout=10).stdout
    else:
        return ""
    return "".join(re.findall(r'"([^"]+)"', out))


def file_token(base: str) -> str:
    try:
        req = urllib.request.Request(base.rstrip("/") + "/.well-known/beril-verify.txt", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read(512).decode("utf-8", "replace").strip()
    except Exception:
        return ""


def meta_token(base: str) -> str:
    try:
        req = urllib.request.Request(base.rstrip("/") + "/", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read(200_000).decode("utf-8", "replace")
    except Exception:
        return ""
    match = re.search(r'<meta[^>]+name=["\']beril-verify["\'][^>]+content=["\']([^"\']+)', body, re.I)
    return match.group(1).strip() if match else ""


def verify(host: str, expected: str, base: str = "") -> dict:
    base = base or f"https://{host}"
    checks = [("dns", lambda: dns_token(host)), ("file", lambda: file_token(base)), ("meta", lambda: meta_token(base))]
    for method, getter in checks:
        try:
            found = getter()
        except Exception:
            found = ""
        if found and hmac.compare_digest(found, expected):
            return record(host, method, expected, f"{method} token matched", "Code verification")
    return record(host, "unverified", expected, "token not found", "Code verification failed")


def require(host: str, owned: bool = False, note: str = "") -> dict | None:
    entry = load(host)
    if entry and entry.get("method") != "unverified":
        return entry
    if owned:
        return record(host, "ack", "", "user said --owned", note or "User declaration")
    return None


def normalize_scope_line(line: str) -> str:
    line = line.strip()
    if not line or line.startswith("#"):
        return ""
    line = re.sub(r"^https?://", "", line)
    return line.split("#", 1)[0].strip().rstrip("/")


def load_scope(path: str | None) -> list[str]:
    if not path:
        return []
    items = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            item = normalize_scope_line(line)
            if item:
                items.append(item)
    return items


def host_matches(host: str, pattern: str) -> bool:
    pattern = pattern.lower().split(":")[0]
    host = host.lower()
    if pattern.startswith("*."):
        return host == pattern[2:] or host.endswith(pattern[1:])
    return host == pattern


def in_scope(url: str, scope: list[str]) -> bool:
    if not scope:
        return True
    from urllib.parse import urlsplit

    parts = urlsplit(url if "://" in url else "https://" + url)
    host = (parts.hostname or "").lower()
    path = parts.path or "/"
    for item in scope:
        if "/" in item:
            pat_host, _, pat_path = item.partition("/")
            pat_path = pat_path.rstrip("*").rstrip("/")
            if host_matches(host, pat_host) and (path == "/" + pat_path or path.startswith("/" + pat_path + "/")):
                return True
            continue
        if host_matches(host, item):
            return True
        try:
            net = ipaddress.ip_network(item, strict=False)
            if parts.hostname and ipaddress.ip_address(parts.hostname) in net:
                return True
        except ValueError:
            pass
    return False


def scope_report(urls: list[str], scope: list[str]) -> dict:
    inside = [u for u in urls if in_scope(u, scope)]
    outside = [u for u in urls if not in_scope(u, scope)]
    return {"in_scope": inside, "out_of_scope": outside}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--new", default="", help="host to issue a token for")
    ap.add_argument("--verify", default="", help="host to verify against the issued token")
    ap.add_argument("--check", default="", help="host to look up")
    ap.add_argument("--base", default="", help="base URL for file and meta methods")
    ap.add_argument("--owned", default="", help="record a human acknowledgement for a host")
    ap.add_argument("--scope", default="", help="scope file to test a URL against")
    ap.add_argument("--url", default="")
    args = ap.parse_args()
    if args.new:
        value = token()
        entry = record(args.new, "pending", value, "token issued", "Not verified yet")
        print(f"host: {entry['host']}\ntoken: {value}\n")
        print(f'DNS:  _beril.{args.new}  TXT  "{value}"')
        print(f"FILE: https://{args.new}/.well-known/beril-verify.txt  content: {value}")
        print(f'META: <meta name="beril-verify" content="{value}">')
        print(f"\nthen: python scripts/authz.py --verify {args.new}")
        return
    if args.verify:
        entry = load(args.verify)
        if not entry:
            sys.exit("issue a token with --new first")
        result = verify(args.verify, entry["token"], args.base)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(0 if result["method"] != "unverified" else 1)
    if args.check:
        entry = load(args.check)
        print(json.dumps(entry or {"valid": False}, indent=2, ensure_ascii=False))
        sys.exit(0 if entry else 1)
    if args.owned:
        print(
            json.dumps(
                record(args.owned, "ack", "", "user said --owned", "User declaration"), indent=2, ensure_ascii=False
            )
        )
        return
    if args.scope and args.url:
        scope = load_scope(args.scope)
        print(json.dumps(scope_report([args.url], scope), indent=2, ensure_ascii=False))
        return
    ap.print_help()


if __name__ == "__main__":
    main()
