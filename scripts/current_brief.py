#!/usr/bin/env python3
"""Build a current-research training brief from the freshest harvest rows.

    ./beril current --limit 10
    ./beril current --source "watchTowr Labs" --out training/current/today.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESEARCH = ("watchTowr Labs", "Horizon3", "Trail of Bits", "PortSwigger Research",
            "Project Zero", "NCC Group", "HackerOne Hacktivity", "Bugcrowd")
LABS = ["web", "binary", "fuzz", "re", "mobile", "firmware", "cloud", "ad", "llm", "detection"]


def load() -> list[dict]:
    path = os.path.join(ROOT, "data", "threads.jsonl")
    if not os.path.exists(path):
        return []
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=8)
    ap.add_argument("--source", default="")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    rows = load()
    if args.source:
        rows = [r for r in rows if r["source"] == args.source]
    else:
        rows = [r for r in rows if r["source"] in RESEARCH]
    rows = [r for r in rows if r.get("url")][: args.limit]

    day = dt.date.today().isoformat()
    out = args.out or os.path.join("training", "current", day + ".md")
    lines = [f"# Current brief, {day}", "",
             "Fresh research turns into drills. Read, answer in writing, then test one idea on a lab.",
             "", "## Reading queue", ""]
    for i, r in enumerate(rows, 1):
        lines += [f"### {i}. [{r['title']}]({r['url']})",
                  f"- Source: {r['source']}",
                  f"- Date: {r.get('date') or 'unknown'}",
                  "- Q1: What is the primitive or root cause?",
                  "- Q2: What is the smallest test that shows it?",
                  "- Q3: Which Beril lab can model it?", ""]

    lines += ["## Drill", "",
              f"- Run `./beril labs --run {random.choice(LABS)}`.",
              "- Pick one item above and write a 150-word method card.",
              "- Add the card to `data/learned_methods.jsonl` with `./beril reflect`.",
              "- Add one question to your review deck.", ""]
    lines += ["## Evidence", "",
              "- Reading notes path:",
              "- Lab output path:",
              "- What changed in your model:", ""]

    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(lines))
    print(f"wrote {out} ({len(rows)} items)")


if __name__ == "__main__":
    main()
