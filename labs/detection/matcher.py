#!/usr/bin/env python3
"""Tiny Sigma-like matcher for the access log lab. Supports endswith and contains."""
import argparse
import re

import yaml

LINE = re.compile(r'^(?P<ip>\S+) .*?"(?P<method>\S+) (?P<uri>\S+) [^"]+" (?P<status>\d+)')


def match(line: str, selection: dict) -> bool:
    m = LINE.match(line)
    if not m:
        return False
    fields = {"cs-uri-stem": m.group("uri").split("?")[0],
              "cs-uri-query": m.group("uri").split("?", 1)[1] if "?" in m.group("uri") else ""}
    for key, cond in selection.items():
        field, _, op = key.partition("|")
        value = fields.get(field, "")
        if op == "endswith" and not value.endswith(cond):
            return False
        if op == "contains":
            values = cond if isinstance(cond, list) else [cond]
            if not any(v in value for v in values):
                return False
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default="access.log")
    ap.add_argument("--rule", default="rules/cgi_injection.yml")
    args = ap.parse_args()
    rule = yaml.safe_load(open(args.rule))
    hits = 0
    for line in open(args.log):
        if match(line, rule["detection"]["selection"]):
            hits += 1
            print(line.rstrip())
    print(f"hits={hits}")


if __name__ == "__main__":
    main()
