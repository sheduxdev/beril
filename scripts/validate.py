#!/usr/bin/env python3
"""Validate the catalog and the prose. Exit code 1 means something needs fixing.

python scripts/validate.py
python scripts/validate.py --links --max-links 40
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import re
import sys
import urllib.request

FILES = {
    "threads.jsonl": ("thread", ("type", "source", "url", "title")),
    "experts.jsonl": ("expert", ("type", "source", "name", "profile")),
    "canonical_tools.jsonl": ("tool", ("type", "category", "repo", "name")),
    "methods.jsonl": ("method", ("type", "source", "url", "title")),
    "method_details.jsonl": ("method", ("type", "source", "url", "title", "headings")),
    "re_tools.jsonl": ("tool", ("type", "category", "repo", "name")),
}


def rows(path: str) -> list[dict]:
    out = []
    for line in open(path, encoding="utf-8"):
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
    ap.add_argument("--data", default="data")
    ap.add_argument("--docs", default=".")
    ap.add_argument("--links", action="store_true", help="send HEAD requests to every URL")
    ap.add_argument("--max-links", type=int, default=40)
    args = ap.parse_args()

    errors, warnings = [], []
    for name, (kind, required) in FILES.items():
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
        ids = collections.Counter(
            (row.get("url") or row.get("repo") or row.get("profile"), row.get("title") or row.get("name"))
            for row in dataset
        )
        dupes = [k for k, n in ids.items() if n > 1]
        if dupes:
            warnings.append(f"{name}: {len(dupes)} duplicate identities, first {dupes[0]}")
        print(f"{name}: {len(dataset)} rows, {sum(1 for r in dataset if r.get('collected_at'))} timestamped")

    # Prose checks from the humanizer rules.
    for path in glob.glob(os.path.join(args.docs, "*.md")) + glob.glob(os.path.join(args.docs, "references", "*.md")):
        text = open(path, encoding="utf-8").read()
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
