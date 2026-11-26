#!/usr/bin/env python3
"""Draw recall cards as quiz questions.

./beril quiz
./beril quiz --tag web --count 5
./beril quiz --mode claim --tag auth --answers
./beril quiz --json
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import remember


def card_text(card: dict, mode: str) -> tuple[str, str]:
    """Build the question and answer for one card.

    Args:
        card: Parsed card.
        mode: test, claim or title.

    Returns:
        Question and answer text.
    """
    title = card.get("title", "")
    claim = card.get("claim", "")
    test = card.get("test", "")
    proof = card.get("proof", "")
    failure = card.get("failure", "")
    if mode == "claim":
        return claim, f"{title}\n\nTest. {test}\n\nProof. {proof}\n\nFailure. {failure}"
    if mode == "title":
        return title, f"{claim}\n\nTest. {test}\n\nProof. {proof}"
    return f"{title}\n\n{test}", f"Claim. {claim}\n\nProof. {proof}\n\nFailure. {failure}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tag", default="", help="filter by tag")
    ap.add_argument("--count", type=int, default=3)
    ap.add_argument("--mode", choices=("test", "claim", "title"), default="test")
    ap.add_argument("--answers", action="store_true", help="print the answer after the question")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    cards = [c for c in remember.load() if c.get("status", "active") == "active"]
    if args.tag:
        needle = args.tag.lower()
        cards = [c for c in cards if needle in [t.lower() for t in c.get("tags", [])]]
    if not cards:
        sys.exit(f"no card for tag: {args.tag}")
    random.shuffle(cards)
    selected = cards[: max(1, args.count)]

    rows = []
    for card in selected:
        question, answer = card_text(card, args.mode)
        rows.append({"id": card["id"], "tags": card.get("tags", []), "question": question, "answer": answer})

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return

    for index, row in enumerate(rows, 1):
        print(f"## {index}. {', '.join(row['tags'])}")
        print(row["question"])
        print()
        if args.answers or not sys.stdin.isatty():
            print(row["answer"])
            print()


if __name__ == "__main__":
    main()
