#!/usr/bin/env python3
"""Show knowledge, lab and reference coverage by domain.

./beril coverage
./beril coverage --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
import remember

DOMAINS = {
    "web": ["web"],
    "api": ["api", "graphql"],
    "auth": ["auth", "oauth", "jwt", "saml", "webauthn"],
    "crypto": ["crypto"],
    "cloud": ["cloud", "aws", "azure", "gcp", "iam"],
    "k8s": ["k8s", "kubernetes", "container"],
    "ad": ["ad", "kerberos", "adcs"],
    "windows": ["win", "wink", "windows"],
    "linux": ["linux", "link", "os"],
    "binary": ["binary", "pwn", "heap", "kernel"],
    "mobile": ["mobile", "android", "ios"],
    "detection": ["detection", "sigma", "edr"],
    "ir": ["ir", "forensics"],
    "supply": ["supply", "supply-chain", "pkg", "cicd"],
    "ai": ["ai", "agent", "llm", "mcp"],
    "firmware": ["firmware"],
    "hardware": ["hardware", "hw"],
    "ot": ["ot"],
    "automotive": ["auto"],
    "medical": ["med"],
    "satellite": ["sat"],
    "mainframe": ["mf"],
    "network": ["network", "net", "dns", "bgp", "tls", "wifi"],
    "osint": ["osint", "recon"],
    "design": ["design", "privacy"],
    "lang": ["lang"],
    "red": ["red", "c2", "opsec"],
    "compliance": ["comp", "legal", "gdpr", "kvkk", "cra", "nis2"],
}

LABS = {
    "web": "web",
    "api": "api",
    "auth": "auth",
    "crypto": "crypto",
    "cloud": "cloud",
    "k8s": "cloud",
    "ad": "ad",
    "windows": "",
    "linux": "",
    "binary": "binary,fuzz,re",
    "mobile": "mobile",
    "detection": "detection",
    "ir": "",
    "supply": "",
    "ai": "llm",
    "firmware": "firmware",
    "hardware": "",
    "ot": "",
    "automotive": "",
    "medical": "",
    "satellite": "",
    "mainframe": "",
    "network": "",
    "osint": "",
    "design": "",
    "lang": "",
    "red": "",
    "compliance": "",
}

REFS = {
    "web": "techniques.md,bug-method-matrix.md",
    "api": "techniques.md",
    "auth": "techniques.md",
    "crypto": "specialist-program.md",
    "cloud": "specialist-program.md,network-protection.md",
    "k8s": "specialist-program.md",
    "ad": "specialist-program.md",
    "windows": "specialist-program.md",
    "linux": "specialist-program.md",
    "binary": "exploit-development.md,reverse-engineering.md",
    "mobile": "mobile-reverse.md",
    "detection": "network-visibility.md,network-curriculum.md",
    "ir": "network-runbook.md,incident-library.md",
    "supply": "specialist-program.md,secrets.md",
    "ai": "specialist-program.md,prompt-injection.md",
    "firmware": "firmware-iot.md",
    "hardware": "firmware-iot.md",
    "ot": "network-protection.md",
    "automotive": "firmware-iot.md",
    "medical": "network-protection.md",
    "satellite": "network-protection.md",
    "mainframe": "specialist-program.md",
    "network": "network-protection.md,network-visibility.md",
    "osint": "osint-toolkit.md,recon.md",
    "design": "senior-bar.md,legal.md",
    "lang": "techniques.md",
    "red": "attacking.md",
    "compliance": "legal.md",
}
TARGET = 20


def count_cards(cards: list[dict]) -> dict[str, int]:
    counts = dict.fromkeys(DOMAINS, 0)
    for card in cards:
        tags = [t.lower() for t in card.get("tags", [])]
        for domain, needles in DOMAINS.items():
            if any(needle in tags for needle in needles):
                counts[domain] += 1
    return counts


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    cards = [c for c in remember.load() if c.get("status", "active") == "active"]
    counts = count_cards(cards)
    lab_dir = os.path.join(paths.ROOT, "labs")
    ref_dir = paths.REFERENCES

    rows = []
    for domain in DOMAINS:
        labs = [name for name in LABS.get(domain, "").split(",") if name and os.path.isdir(os.path.join(lab_dir, name))]
        refs = [
            name for name in REFS.get(domain, "").split(",") if name and os.path.exists(os.path.join(ref_dir, name))
        ]
        score = counts[domain]
        status = "strong" if score >= 30 else "ok" if score >= 10 else "thin"
        rows.append(
            {
                "domain": domain,
                "cards": score,
                "labs": labs,
                "references": refs,
                "status": status,
                "target": TARGET,
            }
        )
    rows.sort(key=lambda row: row["cards"])
    total = len(cards)
    mapped = sum(row["cards"] for row in rows)
    covered = sum(min(row["cards"], row["target"]) for row in rows)

    if args.json:
        print(
            json.dumps(
                {"total_cards": total, "mapped_cards": mapped, "domains": rows, "target_per_domain": TARGET}, indent=2
            )
        )
        return

    print(f"{total} active cards, {mapped} mapped across {len(rows)} domains. Target {TARGET} per domain.")
    print(f"Coverage {covered * 100 // (TARGET * len(rows))} percent.")
    print()
    print("| Domain | Cards | Labs | Refs | Status |")
    print("|---|---:|---|---|---|")
    for row in rows:
        print(
            f"| {row['domain']} | {row['cards']} | {', '.join(row['labs']) or '-'} | {', '.join(row['references']) or '-'} | {row['status']} |"
        )
    thin = [row["domain"] for row in rows if row["status"] == "thin"]
    print()
    print("Next: " + (", ".join(thin) if thin else "all domains above the thin line"))


if __name__ == "__main__":
    main()
