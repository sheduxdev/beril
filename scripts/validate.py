#!/usr/bin/env python3
"""Validate the catalog and the prose. Exit code 1 means something needs fixing.

python scripts/validate.py
python scripts/validate.py --links --max-links 40
"""

from __future__ import annotations

import argparse
import collections
import glob
import ipaddress
import json
import os
import re
import sys
import urllib.request

import paths as paths_mod

FILES = {
    "threads.jsonl": ("thread", ("type", "source", "url", "title")),
    "experts.jsonl": ("expert", ("type", "source", "name", "profile")),
    "canonical_tools.jsonl": ("tool", ("type", "category", "repo", "name")),
    "methods.jsonl": ("method", ("type", "source", "url", "title")),
    "method_details.jsonl": ("method", ("type", "source", "url", "title", "headings")),
    "re_tools.jsonl": ("tool", ("type", "category", "repo", "name")),
    "learned_methods.jsonl": ("method", ("lab", "finding", "root_cause", "fix")),
    "github_atlas.jsonl": ("repo", ("type", "repo", "url", "description")),
    "jobs.jsonl": ("job", ("id", "type", "title", "status")),
}


def rows(path: str) -> list[dict]:
    out = []
    with open(path, encoding="utf-8") as handle:
        lines = handle.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError as exc:
            print(f"  bad JSON in {path}: {exc}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", default=paths_mod.DATA)
    ap.add_argument("--docs", default=paths_mod.ROOT)
    ap.add_argument("--links", action="store_true", help="send HEAD requests to every URL")
    ap.add_argument("--max-links", type=int, default=40)
    args = ap.parse_args()

    errors, warnings = [], []
    for name, (_kind, required) in FILES.items():
        path = os.path.join(args.data, name)
        if not os.path.exists(path):
            warnings.append(f"missing {path}")
            continue
        dataset = rows(path)
        if not dataset:
            warnings.append(f"empty {path}")
            continue
        for i, row in enumerate(dataset, 1):
            for field in required:
                if not str(row.get(field, "")).strip():
                    errors.append(f"{name}:{i} missing {field}")
        if name == "jobs.jsonl":
            ids = collections.Counter(row.get("id") for row in dataset)
        else:
            ids = collections.Counter(
                (row.get("url") or row.get("repo") or row.get("profile"), row.get("title") or row.get("name"))
                for row in dataset
            )
        dupes = [k for k, n in ids.items() if n > 1]
        if dupes:
            warnings.append(f"{name}: {len(dupes)} duplicate identities, first {dupes[0]}")
        print(f"{name}: {len(dataset)} rows, {sum(1 for r in dataset if r.get('collected_at'))} timestamped")

    # Machine data used by the scanners.
    machine = [
        "kev.json",
        "epss.json",
        "secret_providers.json",
        "mcp_rules.json",
        "jar_iocs.json",
        "source_rules.json",
        "cms_vulns.json",
        "osv_seed.json",
        "recon.json",
    ]
    for name in machine:
        path = os.path.join(args.data, name)
        if not os.path.exists(path):
            errors.append(f"missing machine data {path}")
            continue
        try:
            with open(path, encoding="utf-8") as handle:
                payload = json.load(handle)
        except json.JSONDecodeError as exc:
            errors.append(f"{path} is not valid JSON: {exc}")
            continue
        if name == "source_rules.json":
            for i, rule in enumerate(payload.get("rules", [])):
                for field in ("id", "title", "severity", "regex", "impact", "fix"):
                    if not rule.get(field):
                        errors.append(f"{path} rule {i} missing {field}")
        if name == "secret_providers.json" and not payload.get("providers"):
            errors.append(f"{path} has no providers")
        if name == "recon.json":
            for key in (
                "cdn_ranges",
                "ip_headers",
                "risky_ports",
                "auth_paths",
                "subdomain_words",
                "takeovers",
                "tech",
            ):
                if not payload.get(key):
                    errors.append(f"{path} has no {key}")
            for cdn, ranges in payload.get("cdn_ranges", {}).items():
                for cidr in ranges:
                    try:
                        ipaddress.ip_network(cidr, strict=False)
                    except ValueError:
                        errors.append(f"{path}: bad CIDR {cdn} {cidr}")
            for port, item in payload.get("risky_ports", {}).items():
                if not str(port).isdigit() or item.get("severity") not in ("critical", "high", "medium", "low", "info"):
                    errors.append(f"{path}: bad risky port {port}")
                elif not item.get("service"):
                    errors.append(f"{path}: risky port {port} has no service")
            for item in payload.get("tech", []):
                matchers = item.get("header") or item.get("body") or item.get("cookie") or item.get("meta")
                if not item.get("name") or not item.get("category") or not matchers:
                    errors.append(f"{path}: incomplete tech fingerprint {item.get('name', '?')}")
            for item in payload.get("takeovers", []):
                if not item.get("service") or not item.get("cname") or not item.get("body"):
                    errors.append(f"{path}: incomplete takeover fingerprint {item.get('service', '?')}")

    # Prose checks from the humanizer rules.
    paths = glob.glob(os.path.join(args.docs, "*.md"))
    paths += glob.glob(os.path.join(args.docs, "docs", "*.md"))
    paths += glob.glob(os.path.join(args.docs, "references", "*.md")) + glob.glob(
        os.path.join(args.docs, "knowledge", "*.md")
    )
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        if "\u2014" in text or "\u2013" in text:
            errors.append(f"{path} contains an em or en dash")
        for pattern in (r"\bnot just\b", r"\bit'?s not .* it'?s\b", r"\bat its core\b", r"\bthe real question\b"):
            if re.search(pattern, text, re.I):
                warnings.append(f"{path} has a humanizer tell: {pattern}")

    if args.links:
        urls = set()
        for name in FILES:
            for row in rows(os.path.join(args.data, name)):
                url = row.get("url") or row.get("repo") or row.get("profile")
                if url and url.startswith("http"):
                    urls.add(url)
        for url in list(urls)[: args.max_links]:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
            try:
                with urllib.request.urlopen(req, timeout=12) as resp:
                    if resp.status >= 400:
                        warnings.append(f"HTTP {resp.status} {url}")
            except Exception as exc:
                warnings.append(f"link failed {url}: {type(exc).__name__}")

    for warning in warnings[:30]:
        print("WARN", warning)
    for error in errors[:30]:
        print("ERR ", error)
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
