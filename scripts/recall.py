#!/usr/bin/env python3
"""Recall durable knowledge before searching the web.

./beril recall "idor object owner check"
./beril recall "saml signature wrapping" --decide
./beril recall "ghidra rust" --json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "knowledge", "index.json")
STOP = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "have",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "was",
    "with",
    "without",
    "into",
    "not",
    "no",
}


def tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9_]+", (text or "").lower()) if t not in STOP and len(t) > 1]


def cards() -> list[dict]:
    if not os.path.exists(INDEX):
        return []
    try:
        return json.load(open(INDEX, encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def age_days(card: dict) -> int:
    try:
        return (dt.date.today() - dt.date.fromisoformat(card.get("updated", "2000-01-01"))).days
    except ValueError:
        return 9999


def score(query: str, card: dict, avg_len: float, df: Counter, n: int) -> float:
    q = tokens(query)
    if not q:
        return 0
    body = " ".join(str(card.get(k, "")) for k in ("title", "claim", "test", "proof", "failure", "body"))
    title = " ".join(str(card.get(k, "")) for k in ("title", "claim")).lower()
    tags = " ".join(card.get("tags", [])).lower()
    words = tokens(body)
    counts = Counter(words)
    total = 0.0
    for term in q:
        tf = counts.get(term, 0)
        if not tf:
            continue
        idf = math.log(1 + (n - df.get(term, 0) + 0.5) / (df.get(term, 0) + 0.5))
        denom = tf + 1.2 * (0.25 + 0.75 * len(words) / max(1, avg_len))
        total += idf * (tf * 2.2) / denom
        if term in title:
            total += 2.2
        if term in tags:
            total += 1.4
    return round(total, 2)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--decide", action="store_true")
    ap.add_argument("--max-chars", type=int, default=4000)
    args = ap.parse_args()

    data = cards()
    if not data:
        print("No knowledge index. Run ./beril remember index")
        return
    df = Counter()
    lengths = []
    for c in data:
        text = " ".join(str(c.get(k, "")) for k in ("title", "claim", "test", "proof", "failure", "body"))
        toks = set(tokens(text))
        lengths.append(len(tokens(text)))
        for t in toks:
            df[t] += 1
    avg = sum(lengths) / max(1, len(lengths))
    ranked = sorted(((score(args.query, c, avg, df, len(data)), c) for c in data), key=lambda x: x[0], reverse=True)
    ranked = [x for x in ranked if x[0] > 0][: args.limit]

    if args.json:
        print(json.dumps([{"score": s, **c} for s, c in ranked], ensure_ascii=False, indent=1))
        return

    if not ranked:
        print("No match. RESEARCH.")
        return

    used = 0
    for s, c in ranked:
        age = age_days(c)
        line = f"[{c['id']}] score={s} confidence={c.get('confidence', '?')} age={age}d\n  {c['title']}\n  {c.get('claim', '')[:220]}\n  test: {c.get('test', '')[:200]}\n  source: {', '.join(c.get('sources', []))}\n"
        if used + len(line) > args.max_chars:
            break
        print(line)
        used += len(line)

    if args.decide:
        s, c = ranked[0]
        age = age_days(c)
        if s >= 5 and c.get("confidence") in ("high", "medium") and age <= 180:
            print(f"DECISION: USE {c['id']}")
        elif s >= 2:
            print(f"DECISION: REFRESH {c['id']}")
        else:
            print("DECISION: RESEARCH")


if __name__ == "__main__":
    main()
