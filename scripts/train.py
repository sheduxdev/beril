#!/usr/bin/env python3
"""Training coach for the Beril curriculum.

    ./beril train --status
    ./beril train --week 1
    ./beril train --next
    ./beril train --done w1d1
    ./beril train --log "Bandit 5 done, learned about setuid"
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRICULUM = os.path.join(ROOT, "data", "curriculum.json")
STATE_DIR = os.path.join(ROOT, "training")
STATE = os.path.join(STATE_DIR, "progress.json")


def load_curriculum() -> dict:
    return json.load(open(CURRICULUM, encoding="utf-8"))


def load_state() -> dict:
    os.makedirs(STATE_DIR, exist_ok=True)
    if os.path.exists(STATE):
        try:
            return json.load(open(STATE, encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"done": [], "journal": [], "started": dt.date.today().isoformat()}


def save_state(state: dict) -> None:
    os.makedirs(STATE_DIR, exist_ok=True)
    json.dump(state, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def tasks(week: dict) -> list[dict]:
    out = list(week["drills"]) + [week["deliverable"]]
    for item in out:
        item["week"] = week["week"]
    return out


def all_tasks(curriculum: dict) -> list[dict]:
    out = []
    for week in curriculum["weeks"]:
        out += tasks(week)
    return out


def find_week(curriculum: dict, number: int) -> dict | None:
    return next((w for w in curriculum["weeks"] if w["week"] == number), None)


def show_week(week: dict, state: dict) -> str:
    lines = [f"# Week {week['week']}: {week['title']}", "",
             f"Phase: {week['phase']}  Time: about {week['minutes']} min", "",
             f"Goal: {week['goal']}", "", "## Drills"]
    for d in week["drills"]:
        mark = "x" if d["key"] in state["done"] else " "
        lines.append(f"- [{mark}] {d['text']} ({d['minutes']} min)  `{d['key']}`")
    lines += ["", "## Lab", f"- {week['lab']}", "", "## Reading", f"- {week['reading']}", "",
              "## Checkpoint", f"- {week['checkpoint']}", "", "## Deliverable"]
    d = week["deliverable"]
    mark = "x" if d["key"] in state["done"] else " "
    lines.append(f"- [{mark}] {d['text']}  `{d['key']}`")
    lines += ["", "Mark a task: `./beril train --done <key>`"]
    return "\n".join(lines)


def status(curriculum: dict, state: dict) -> str:
    every = all_tasks(curriculum)
    done = len([t for t in every if t["key"] in state["done"]])
    pct = done * 100 // max(1, len(every))
    next_tasks = [t for t in every if t["key"] not in state["done"]][:3]
    lines = [f"Progress: {done}/{len(every)} tasks ({pct}%)", ""]
    if next_tasks:
        lines.append("Next:")
        for t in next_tasks:
            lines.append(f"- Week {t['week']}: {t['text']}  `{t['key']}`")
    else:
        lines.append("Curriculum complete. Start the capstone again with a new target.")
    lines += ["", f"Journal entries: {len(state['journal'])}", "Open a week: `./beril train --week <n>`"]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--week", type=int)
    ap.add_argument("--phase", type=int)
    ap.add_argument("--next", action="store_true")
    ap.add_argument("--done", default="")
    ap.add_argument("--log", default="")
    args = ap.parse_args()

    curriculum, state = load_curriculum(), load_state()

    if args.log:
        state["journal"].append({"at": dt.datetime.now().isoformat(timespec="minutes"), "text": args.log})
        save_state(state)
        print("logged")
        return

    if args.done:
        valid = {t["key"]: t for t in all_tasks(curriculum)}
        if args.done not in valid:
            sys.exit(f"unknown task: {args.done}")
        if args.done not in state["done"]:
            state["done"].append(args.done)
            save_state(state)
        task = valid[args.done]
        print(f"done: {task['text']}")
        print(status(curriculum, state))
        return

    if args.week is not None:
        week = find_week(curriculum, args.week)
        if not week:
            sys.exit(f"no week {args.week}")
        print(show_week(week, state))
        return

    if args.phase is not None:
        phases = curriculum["phases"]
        if not 0 <= args.phase < len(phases):
            sys.exit(f"phase index 0 to {len(phases) - 1}")
        for number in phases[args.phase]["weeks"]:
            week = find_week(curriculum, number)
            if week:
                print(show_week(week, state))
                print("\n---\n")
        return

    if args.next:
        remaining = [t for t in all_tasks(curriculum) if t["key"] not in state["done"]]
        if not remaining:
            print("nothing left")
        else:
            t = remaining[0]
            week = find_week(curriculum, t["week"])
            print(show_week(week, state))
        return

    print(status(curriculum, state))


if __name__ == "__main__":
    main()
