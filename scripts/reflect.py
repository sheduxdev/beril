#!/usr/bin/env python3
"""Turn a finished lab into a durable method note.

    ./beril reflect --lab web --finding "IDOR on /profile" \
      --root-cause "query id overrides session" --evidence labs/web/shot.png \
      --fix "scope by session uid"
    ./beril reflect --list
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random

import paths

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(paths.DATA, "learned_methods.jsonl")


def load() -> list[dict]:
    if not os.path.exists(OUT):
        return []
    return [json.loads(line) for line in open(OUT, encoding="utf-8") if line.strip()]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lab", default="")
    ap.add_argument("--finding", default="")
    ap.add_argument("--root-cause", default="")
    ap.add_argument("--evidence", default="")
    ap.add_argument("--fix", default="")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--review", action="store_true")
    args = ap.parse_args()

    rows = load()

    if args.list:
        for r in rows:
            print(f"[{r['lab']}] {r['finding']}  ({r['at'][:10]})")
        print(f"{len(rows)} learned methods")
        return

    if args.review:
        for r in random.sample(rows, min(3, len(rows))):
            print(f"[{r['lab']}] {r['finding']}")
            print(f"  cause: {r['root_cause']}")
            print(f"  fix: {r['fix']}")
        return

    if not (args.lab and args.finding and args.root_cause and args.fix):
        ap.error("--lab, --finding, --root-cause and --fix are required")

    row = {
        "lab": args.lab,
        "finding": args.finding,
        "root_cause": args.root_cause,
        "evidence": args.evidence,
        "fix": args.fix,
        "at": dt.datetime.now().isoformat(timespec="minutes"),
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"learned: {args.finding}")
    print(f"total: {len(rows) + 1}")


if __name__ == "__main__":
    main()
