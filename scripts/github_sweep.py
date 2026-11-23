#!/usr/bin/env python3
"""Sweep GitHub security topics into a single atlas.

export GITHUB_TOKEN=...   # optional, raises the search limit
python scripts/github_sweep.py --out data/github_atlas.jsonl --per-query 30
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
import urllib.parse
import urllib.request

QUERIES = {
    "bug-bounty": ["topic:bug-bounty", "topic:bugbounty", "bug bounty automation", "bug bounty methodology"],
    "pentest": ["topic:penetration-testing", "topic:pentest", "pentest framework", "pentest automation"],
    "red-team": ["topic:red-team", "topic:redteam", "topic:offensive-security", "red team tool"],
    "web-security": [
        "topic:web-security",
        "topic:application-security",
        "web application security",
        "topic:api-security",
    ],
    "cloud-security": [
        "topic:cloud-security",
        "topic:aws-security",
        "topic:kubernetes-security",
        "topic:container-security",
    ],
    "recon": ["topic:reconnaissance", "topic:subdomain", "topic:osint", "attack surface management"],
    "binary": [
        "topic:reverse-engineering",
        "topic:binary-analysis",
        "topic:exploit-development",
        "topic:malware-analysis",
    ],
    "ghidra": ["topic:ghidra", "ghidra plugin", "ghidra scripts"],
    "ida-binja": ["topic:ida-plugin", "topic:binaryninja", "topic:radare2"],
    "fuzzing": ["topic:fuzzing", "fuzzer", "coverage guided fuzzing"],
    "vuln-research": ["topic:vulnerability-research", "topic:vulnerability-scanner", "topic:exploit", "topic:cve"],
    "detection": [
        "topic:threat-hunting",
        "topic:detection-engineering",
        "topic:incident-response",
        "topic:digital-forensics",
    ],
    "blue-team": ["topic:blue-team", "topic:siem", "topic:soc", "topic:security-monitoring"],
    "supply-chain": ["topic:supply-chain-security", "topic:devsecops", "topic:sbom", "topic:secret-scanning"],
    "mobile": [
        "topic:mobile-security",
        "topic:android-security",
        "topic:ios-security",
        "topic:android-reverse-engineering",
    ],
    "firmware": ["topic:firmware", "topic:iot-security", "topic:hardware-security", "firmware analysis"],
    "wireless": ["topic:wireless-security", "wifi hacking", "bluetooth security"],
    "crypto": ["topic:cryptography", "topic:tls", "cryptographic audit"],
    "web3": ["topic:smart-contract", "topic:web3-security", "solidity security", "smart contract audit"],
    "ctf": ["topic:ctf", "topic:ctf-tools", "topic:pwn", "capture the flag security"],
    "toolkit": ["topic:security-tools", "topic:hacking-tools", "topic:awesome-security", "security cheatsheet"],
    "data": ["topic:wordlists", "topic:payloads", "topic:security-datasets", "topic:exploit-db"],
    "ad": ["topic:active-directory", "topic:privilege-escalation", "active directory security"],
    "hardening": ["topic:linux-hardening", "topic:windows-security", "topic:security-hardening"],
    "burp": ["topic:burp-extension", "burp suite extension", "topic:caido"],
    "ai-security": ["topic:llm-security", "topic:ai-security", "prompt injection"],
}


def token() -> str:
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    try:
        return subprocess.check_output(["gh", "auth", "token"], text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ""


def get(url: str, tok: str, retries: int = 5) -> dict:
    for attempt in range(retries):
        req = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "beril-github-sweep",
                **({"Authorization": "Bearer " + tok} if tok else {}),
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                return json.load(resp)
        except Exception as exc:
            msg = str(exc)
            wait = 20 + attempt * 20
            if "403" in msg or "429" in msg:
                wait = 65
            print(f"  retry {attempt + 1} in {wait}s: {msg[:90]}")
            time.sleep(wait)
    return {}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="data/github_atlas.jsonl")
    ap.add_argument("--per-query", type=int, default=30)
    ap.add_argument("--min-stars", type=int, default=15)
    args = ap.parse_args()

    tok = token()
    seen: dict[str, dict] = {}
    for category, queries in QUERIES.items():
        for q in queries:
            url = (
                "https://api.github.com/search/repositories?q="
                + urllib.parse.quote(q)
                + f"&sort=stars&order=desc&per_page={args.per_query}"
            )
            data = get(url, tok)
            items = data.get("items", [])
            new = 0
            for item in items:
                if item.get("stargazers_count", 0) < args.min_stars:
                    continue
                repo = item["full_name"]
                if repo in seen:
                    if category not in seen[repo]["categories"]:
                        seen[repo]["categories"].append(category)
                    continue
                seen[repo] = {
                    "type": "repo",
                    "repo": repo,
                    "name": repo,
                    "url": item.get("html_url", ""),
                    "description": (item.get("description") or "")[:350],
                    "stars": item.get("stargazers_count", 0),
                    "forks": item.get("forks_count", 0),
                    "language": item.get("language") or "",
                    "license": (item.get("license") or {}).get("spdx_id", ""),
                    "archived": item.get("archived", False),
                    "updated": item.get("pushed_at", ""),
                    "topics": item.get("topics", [])[:15],
                    "categories": [category],
                    "query": q,
                }
                new += 1
            print(f"{category:<15} {q:<42} {len(items):>3} new={new} total={len(seen)}")
            time.sleep(2)

    rows = sorted(seen.values(), key=lambda r: r["stars"], reverse=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"wrote {len(rows)} -> {args.out}")


if __name__ == "__main__":
    main()
