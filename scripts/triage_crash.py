#!/usr/bin/env python3
"""Sanitizer output parser and crash dedupe.

Reads a log, names the primitive, hashes the top stack frames and produces a
finding only when a real sanitizer signature exists. A timeout or a non-zero
exit without a signature stays a build note.

    python scripts/triage_crash.py --log run.log --target ./repo
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from beril_model import Finding

SIGNATURES = [
    ("heap-buffer-overflow", "critical", "Heap overflow"),
    ("stack-buffer-overflow", "high", "Stack overflow"),
    ("global-buffer-overflow", "high", "Global overflow"),
    ("heap-use-after-free", "high", "Use after free (UAF)"),
    ("stack-use-after-return", "high", "Stack use after return"),
    ("use-after-poison", "high", "Use after poison"),
    ("SEGV on unknown address", "medium", "Segfault"),
    ("undefined-behavior", "medium", "Undefined behavior (UBSan)"),
    ("signed integer overflow", "medium", "Signed integer overflow"),
    ("data race", "medium", "Data race (TSan)"),
    ("runtime error:", "low", "UBSan warning"),
    ("allocation-size-too-big", "medium", "Oversized allocation"),
    ("double-free", "high", "Double free"),
    ("memory leak", "low", "Memory leak"),
    ("stack-overflow", "medium", "Stack exhaustion"),
]

FRAME = re.compile(r"#\d+\s+0x[0-9a-f]+\s+in\s+(\S+)\s+(?:(\S+):(\d+))?")
SUMMARY = re.compile(r"SUMMARY:\s+(\S+):\s+(\S+)")


def triage(log: str, target: str, input_path: str = "") -> list[Finding]:
    found = []
    hits = []
    for needle, severity, label in SIGNATURES:
        if needle.lower() in log.lower():
            hits.append((needle, severity, label))
    if not hits:
        if "timeout" in log.lower():
            found.append(
                Finding(
                    check="crash.timeout",
                    title="Run timed out",
                    severity="low",
                    confidence="medium",
                    evidence=f"{target}: timeout",
                    impact="A hang or infinite loop is possible.",
                    fix="Shrink the input and reproduce with a longer timeout.",
                    subject=target,
                    source="triage",
                    state="inferred",
                )
            )
        return found
    frames = FRAME.findall(log)
    signature = "|".join(f[0] for f in frames[:5]) or hits[0][0]
    digest = hashlib.sha1(signature.encode()).hexdigest()[:12]
    for needle, severity, label in hits[:3]:
        finding = Finding(
            check="crash." + re.sub(r"\W+", "-", needle).strip("-").lower(),
            title=f"Sanitizer: {label}",
            severity=severity,
            confidence="high",
            evidence=f"{target}: {needle}, dupe {digest}" + (f", girdi {input_path}" if input_path else ""),
            impact="Memory corruption or undefined behavior. Exploitability still needs proof.",
            fix="Keep the smallest input, add the sanitizer build to CI and fix the root cause.",
            subject=target,
            source="triage",
            state="observed",
            verified=True,
            cwe=["CWE-787"] if "buffer" in needle else ["CWE-416"] if "free" in needle else ["CWE-20"],
            false_positive="The sanitizer finding is real, but DoS or RCE stays unclaimed until proven.",
        )
        finding.id = f"crash-{digest}-{re.sub(r'[^a-z0-9]+', '-', needle)[:20]}"
        found.append(finding)
    return found


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--log", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--input", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    with open(args.log, encoding="utf-8", errors="replace") as handle:
        log = handle.read()
    findings = triage(log, args.target, args.input)
    print(
        json.dumps([f.to_dict() for f in findings], indent=2, ensure_ascii=False)
        if args.json
        else "\n".join(f"[{f.severity}] {f.title}: {f.evidence}" for f in findings) or "no signature"
    )


if __name__ == "__main__":
    main()
