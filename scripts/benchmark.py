#!/usr/bin/env python3
"""Measure precision and recall on the labeled corpora in ``benchmarks/``.

The numbers are file level. A source finding anywhere in a file is a positive.
A secret positive counts only when the expected provider fires; any hit on a
negative is a false positive. CVE cases match the expected OSV id.

This is a detector benchmark, not a product comparison. Adapters, reachability
and online data are out of scope.

    python scripts/benchmark.py --corpus all
    python scripts/benchmark.py --corpus secrets --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import beril_secrets
import deps
import paths
import source_audit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CORPORA = paths.BENCHMARKS
LANG = {".java": "java", ".c": "c", ".py": "python", ".js": "javascript", ".ts": "typescript"}


def empty() -> dict:
    return {"tp": 0, "fp": 0, "fn": 0, "tn": 0}


def score(counts: dict) -> dict:
    tp, fp, fn = counts["tp"], counts["fp"], counts["fn"]
    precision = round(tp / (tp + fp), 3) if tp + fp else None
    recall = round(tp / (tp + fn), 3) if tp + fn else None
    return {**counts, "precision": precision, "recall": recall}


def source_corpus(section: dict) -> dict:
    per_category: dict[str, dict] = {}
    for name, label in section["cases"].items():
        source = (
            os.path.join(CORPORA, "owasp", name) if name.endswith(".java") else os.path.join(CORPORA, "juliet", name)
        )
        try:
            text = Path(source).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        findings = source_audit.scan_text(name, text, LANG.get(Path(name).suffix, ""))
        flagged = bool(findings)
        category = label.get("category", "unknown")
        row = per_category.setdefault(category, empty())
        if label["vulnerable"] and flagged:
            row["tp"] += 1
        elif label["vulnerable"]:
            row["fn"] += 1
        elif flagged:
            row["fp"] += 1
        else:
            row["tn"] += 1
    total = empty()
    for row in per_category.values():
        for key in total:
            total[key] += row[key]
    return {"total": score(total), "categories": {k: score(v) for k, v in sorted(per_category.items())}}


def secret_corpus(section: dict) -> dict:
    counts = empty()
    for name, provider in section["positives"].items():
        text = (Path(CORPORA) / "secrets" / name).read_text(encoding="utf-8", errors="replace")
        found = {finding.check for finding in beril_secrets.scan_text(name, text)}
        if f"secret.{provider}" in found:
            counts["tp"] += 1
        else:
            counts["fn"] += 1
        counts["fp"] += len(found - {f"secret.{provider}"})
    for name in section["negatives"]:
        text = (Path(CORPORA) / "secrets" / name).read_text(encoding="utf-8", errors="replace")
        hits = beril_secrets.scan_text(name, text)
        if hits:
            counts["fp"] += 1
        else:
            counts["tn"] += 1
    return {"total": score(counts), "categories": {}}


def cve_corpus(section: dict) -> dict:
    counts = empty()
    for name, label in section["cases"].items():
        report = deps.scan(os.path.join(CORPORA, "cve", name))
        checks = " ".join(finding.check for finding in report.findings)
        expected = label.get("cve", "").replace("-", ".").lower()
        hit = bool(expected) and expected in checks.lower()
        if label["vulnerable"] and hit:
            counts["tp"] += 1
        elif label["vulnerable"]:
            counts["fn"] += 1
        elif report.findings:
            counts["fp"] += 1
        else:
            counts["tn"] += 1
    return {"total": score(counts), "categories": {}}


def run(selected: list[str]) -> dict:
    manifest = json.loads((Path(CORPORA) / "manifest.json").read_text(encoding="utf-8"))
    runners = {"owasp": source_corpus, "juliet": source_corpus, "secrets": secret_corpus, "cve": cve_corpus}
    out = {}
    for name in selected:
        if name in runners and name in manifest:
            out[name] = runners[name](manifest[name])
    return out


def markdown(results: dict) -> str:
    lines = [
        "# Detector benchmarks",
        "",
        "File-level precision and recall on the corpus in `benchmarks/`. A missing",
        "number means the denominator was zero. The corpus is small; treat the",
        "numbers as a direction, not a certificate.",
        "",
        "| Corpus | TP | FP | FN | TN | Precision | Recall |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for name, data in results.items():
        total = data["total"]
        precision = "-" if total["precision"] is None else f"{total['precision']:.3f}"
        recall = "-" if total["recall"] is None else f"{total['recall']:.3f}"
        lines.append(
            f"| {name} | {total['tp']} | {total['fp']} | {total['fn']} | {total['tn']} | {precision} | {recall} |"
        )
    lines += ["", "## By category", ""]
    for name, data in results.items():
        if not data["categories"]:
            continue
        lines += [f"### {name}", "", "| Category | TP | FP | FN | Recall |", "|---|---:|---:|---:|---:|"]
        for category, row in data["categories"].items():
            recall = "-" if row["recall"] is None else f"{row['recall']:.3f}"
            lines.append(f"| {category} | {row['tp']} | {row['fp']} | {row['fn']} | {recall} |")
        lines.append("")
    lines += [
        "## Method",
        "",
        "```bash",
        "python scripts/benchmark.py --corpus all",
        "```",
        "",
        "Source corpora live under `benchmarks/owasp` and `benchmarks/juliet`.",
        "Provenance and licences are in `benchmarks/README.md`.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus", default="all", choices=("all", "owasp", "juliet", "secrets", "cve"))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    selected = ["owasp", "juliet", "secrets", "cve"] if args.corpus == "all" else [args.corpus]
    results = run(selected)
    print(json.dumps(results, indent=2) if args.json else markdown(results))
    if args.out:
        Path(args.out).write_text(markdown(results) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
