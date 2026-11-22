#!/usr/bin/env python3
"""Append-only job ledger for scans, labs, harvests and LLM work.

    ./beril job start --type llm --title "Triage CVE notes" --model claude-sonnet-4.5
    ./beril job finish --id ab12cd34 --status done --tokens-in 12000 --tokens-out 800
    ./beril job log --type scan --title "example.com" --status done
    ./beril job list --limit 20
    ./beril job budget --set 25
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import secrets

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "data", "jobs.jsonl")
PRICES = os.path.join(ROOT, "data", "llm_prices.json")
BUDGET = os.path.join(ROOT, "data", "budget.json")


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def price(model: str) -> tuple[float, float]:
    if not os.path.exists(PRICES):
        return 0.0, 0.0
    data = json.load(open(PRICES))
    row = data.get(model) or data.get("default") or {}
    return float(row.get("in", 0)), float(row.get("out", 0))


def append(row: dict) -> None:
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def load() -> list[dict]:
    if not os.path.exists(LEDGER):
        return []
    out = []
    for line in open(LEDGER, encoding="utf-8"):
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def update(job_id: str, patch: dict) -> dict | None:
    rows = load()
    found = None
    for row in rows:
        if row["id"] == job_id:
            row.update(patch)
            found = row
            break
    if found:
        with open(LEDGER, "w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return found


def create(args) -> dict:
    job = {
        "id": secrets.token_hex(4), "type": args.type, "title": args.title,
        "status": args.status, "actor": args.actor, "model": args.model or "",
        "target": args.target or "", "parent": args.parent or "",
        "started_at": now(), "finished_at": now() if args.status != "running" else "",
        "tokens_in": int(args.tokens_in or 0), "tokens_out": int(args.tokens_out or 0),
        "cost_usd": 0.0, "log": args.log or "", "notes": args.notes or "",
    }
    pin, pout = price(job["model"])
    computed = (job["tokens_in"] / 1_000_000 * pin) + (job["tokens_out"] / 1_000_000 * pout)
    job["cost_usd"] = round(float(args.cost or 0) or computed, 6)
    append(job)
    return job


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--type", choices=["llm", "scan", "lab", "harvest", "report", "manual"], default="manual")
        p.add_argument("--title", required=True)
        p.add_argument("--status", choices=["running", "done", "failed", "cancelled"], default="running")
        p.add_argument("--actor", default="agent")
        p.add_argument("--model", default="")
        p.add_argument("--target", default="")
        p.add_argument("--parent", default="")
        p.add_argument("--tokens-in", type=int, default=0)
        p.add_argument("--tokens-out", type=int, default=0)
        p.add_argument("--cost", type=float, default=0)
        p.add_argument("--log", default="")
        p.add_argument("--notes", default="")

    p = sub.add_parser("start")
    common(p)
    p = sub.add_parser("log")
    common(p)
    p = sub.add_parser("finish")
    p.add_argument("--id", required=True)
    p.add_argument("--status", choices=["done", "failed", "cancelled"], default="done")
    p.add_argument("--model", default="")
    p.add_argument("--tokens-in", type=int, default=0)
    p.add_argument("--tokens-out", type=int, default=0)
    p.add_argument("--cost", type=float, default=0)
    p.add_argument("--log", default="")
    p.add_argument("--notes", default="")
    p = sub.add_parser("list")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--status", default="")
    p = sub.add_parser("budget")
    p.add_argument("--set", type=float, default=None)

    args = ap.parse_args()
    if args.cmd in ("start", "log"):
        job = create(args)
        print(job["id"])
        print(f"{job['type']} {job['status']} {job['title']} ${job['cost_usd']:.4f}")
    elif args.cmd == "finish":
        pin, pout = price(args.model)
        patch = {"status": args.status, "finished_at": now(), "tokens_in": args.tokens_in,
                 "tokens_out": args.tokens_out, "log": args.log, "notes": args.notes}
        if args.cost:
            patch["cost_usd"] = round(args.cost, 6)
        elif args.tokens_in or args.tokens_out:
            patch["cost_usd"] = round(args.tokens_in / 1_000_000 * pin + args.tokens_out / 1_000_000 * pout, 6)
        row = update(args.id, patch)
        print(json.dumps(row, ensure_ascii=False) if row else "not found")
    elif args.cmd == "list":
        rows = load()
        if args.status:
            rows = [r for r in rows if r["status"] == args.status]
        for r in rows[-args.limit:]:
            print(f"{r['id']} {r['status']:<9} {r['type']:<8} ${r['cost_usd']:.4f} {r['title'][:70]}")
    elif args.cmd == "budget":
        current = json.load(open(BUDGET)) if os.path.exists(BUDGET) else {"monthly_usd": 25}
        if args.set is not None:
            current["monthly_usd"] = args.set
            json.dump(current, open(BUDGET, "w"), indent=1)
        print(json.dumps(current))


if __name__ == "__main__":
    main()
