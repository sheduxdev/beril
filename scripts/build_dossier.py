#!/usr/bin/env python3
"""Merge harvested JSONL into a readable dossier with links and gaps.

Example
-------
python scripts/build_dossier.py --data data --out examples/dossier.md
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import re


def rows(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    out = []
    for line in open(path, encoding="utf-8"):
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return out


def stars(value) -> float:
    text = str(value or "").lower().replace(",", "").replace("$", "")
    text = re.sub(r"[^0-9.k]", "", text)
    if not text:
        return 0.0
    try:
        return float(text[:-1]) * 1000 if text.endswith("k") else float(text)
    except ValueError:
        return 0.0


def esc(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip().replace("|", "\\|")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", default="data")
    ap.add_argument("--out", default="examples/dossier.md")
    ap.add_argument("--title", default="Cyber intelligence dossier")
    ap.add_argument("--top", type=int, default=12)
    args = ap.parse_args()

    threads = rows(os.path.join(args.data, "threads.jsonl"))
    experts = rows(os.path.join(args.data, "experts.jsonl"))
    tools = rows(os.path.join(args.data, "canonical_tools.jsonl")) or rows(os.path.join(args.data, "tools.jsonl"))
    tools += rows(os.path.join(args.data, "re_tools.jsonl"))
    methods = rows(os.path.join(args.data, "method_details.jsonl")) or rows(os.path.join(args.data, "methods.jsonl"))

    lines: list[str] = []
    add = lines.append
    today = dt.date.today().isoformat()
    add(f"# {args.title}")
    add("")
    add(f"Collected {today}. Every entry links to its public source. Counts describe this snapshot, not the whole internet.")
    add("")

    add("## Coverage")
    add("")
    add("| Layer | Rows | Sources |")
    add("|---|---:|---|")
    for label, dataset in (("Threads and reports", threads), ("Experts", experts), ("Tools", tools), ("Methods and research", methods)):
        add(f"| {label} | {len(dataset)} | {len({r.get('source', '') for r in dataset})} |")
    add("")

    if threads:
        add("## High-signal threads")
        add("")
        cool = sorted(
            threads,
            key=lambda r: (stars(r.get("metrics", {}).get("bounty", "")),
                           stars(r.get("metrics", {}).get("score", "")),
                           float(r.get("metrics", {}).get("replies") or 0)),
            reverse=True,
        )[: args.top]
        for r in cool:
            meta = []
            for key in ("program", "weakness", "severity", "bounty", "score", "replies"):
                value = r.get("metrics", {}).get(key)
                if value:
                    meta.append(f"{key} {value}")
            add(f"- [{esc(r.get('title'))}]({r.get('url')})")
            if meta:
                add(f"  {esc(', '.join(str(m) for m in meta))} ({esc(r.get('source', ''))})")
        add("")

    if experts:
        add("## Experts worth reading")
        add("")
        ranked = sorted(experts, key=lambda r: (len(r.get("works", [])), r.get("name", "")), reverse=True)
        for e in ranked[: args.top]:
            add(f"- [{esc(e.get('name'))}]({e.get('profile')}) - {esc(e.get('focus'))}")
            for work in e.get("works", [])[:2]:
                add(f"  - [{esc(work.get('title'))}]({work.get('url')})")
        add("")

    if tools:
        add("## Tool shelf")
        add("")
        by_cat = collections.defaultdict(list)
        for t in tools:
            by_cat[t.get("category") or t.get("topic") or "other"].append(t)
        for cat in sorted(by_cat):
            shelf = sorted(by_cat[cat], key=lambda r: stars(r.get("stars")), reverse=True)[: args.top]
            add(f"### {cat.replace('_', ' ')}")
            add("")
            for t in shelf:
                desc = esc(t.get("description"))[:120]
                add(f"- [{t.get('name')}]({t.get('repo')}) - {t.get('stars', '?')} stars. {desc}")
            add("")

    if methods:
        add("## Method index")
        add("")
        for m in methods[: max(args.top * 4, 40)]:
            extra = f" ({m.get('code_blocks')} code blocks)" if m.get("code_blocks") else ""
            add(f"- [{esc(m.get('title'))}]({m.get('url')}) - {esc(m.get('source', ''))}{extra}")
        add("")

    add("## Gaps and next passes")
    add("")
    if not threads:
        add("- No threads. Run `harvest.py forums` and check that the cache directory is writable.")
    if not experts:
        add("- No experts. Run `harvest.py experts --sources curated,hackerone`.")
    if not tools:
        add("- No tools. Run `harvest.py tools --sources canonical`.")
    if not methods:
        add("- No methods. Run `harvest.py methods` and `extract.py`.")
    if threads and sum(1 for t in threads if t.get("summary")) / len(threads) < 0.5:
        add("- Fewer than half of the threads have summaries. Run `extract.py` on the top URLs.")
    add("- Re-run monthly. Forum threads and tool stars move; disclosed reports age out of the first pages.")
    add("")

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    open(args.out, "w", encoding="utf-8").write("\n".join(lines))
    print(f"wrote {args.out} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
