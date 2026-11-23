#!/usr/bin/env python3
"""Static review of local infrastructure config: Terraform, Kubernetes, Docker, CloudFormation.

This is the local CSPM gap. It reads files, never calls a cloud API. A hit is a
review lead with a line and a fix.

    ./beril infra --target ./terraform
    ./beril infra --target ./k8s --json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections.abc import Iterator

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paths
import report_render
import suppress
from beril_model import Finding, Report, load_report

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKIP = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".terraform"}
EXT = {".tf", ".yaml", ".yml", ".json", ".template", ".dockerfile"}
DOCKER_NAMES = {"Dockerfile", "docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml"}
MAX_FILES = 4000


def load_rules() -> list[dict]:
    try:
        with open(os.path.join(paths.DATA, "infra_rules.json"), encoding="utf-8") as handle:
            return json.load(handle).get("rules", [])
    except (OSError, json.JSONDecodeError):
        return []


def iter_files(root: str) -> Iterator[str]:
    if os.path.isfile(root):
        yield root
        return
    count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in filenames:
            if os.path.splitext(name)[1].lower() in EXT or name in DOCKER_NAMES:
                yield os.path.join(dirpath, name)
                count += 1
                if count >= MAX_FILES:
                    return


def scan(target: str) -> Report:
    report = Report(target=target, mode="source")
    report.scope["checked"] = [
        "Terraform",
        "Kubernetes YAML",
        "Dockerfile and compose",
        "CloudFormation",
        "Line numbers and fixes",
    ]
    report.scope["not_checked"] = ["Cloud API state", "Plan or applied config", "Runtime drift", "Secret values"]
    if not os.path.exists(target):
        report.errors.append("target missing")
        return report.finish()
    rules = load_rules()
    files = list(iter_files(target))
    if not files:
        report.errors.append("no infrastructure file found")
        return report.finish()
    kinds = {"terraform": [], "k8s": [], "docker": [], "cfn": []}
    for path in files:
        name = os.path.basename(path)
        ext = os.path.splitext(name)[1].lower()
        try:
            with open(path, encoding="utf-8", errors="replace") as handle:
                text = handle.read(400_000)
        except OSError:
            continue
        if ext == ".tf":
            kinds["terraform"].append((path, text))
        elif name in DOCKER_NAMES:
            kinds["docker"].append((path, text))
        elif ext in (".template",) or "AWSTemplateFormatVersion" in text[:500]:
            kinds["cfn"].append((path, text))
        elif ext in (".yaml", ".yml") and re.search(r"^apiVersion\s*:", text, re.M):
            kinds["k8s"].append((path, text))
        for rule in rules:
            for match in re.finditer(rule["regex"], text, re.M):
                line = text[: match.start()].count("\n") + 1
                report.add(
                    Finding(
                        check="infra." + rule["id"],
                        title=rule["title"],
                        severity=rule["severity"],
                        confidence=rule["confidence"],
                        evidence=f"{path}:{line} {match.group(0)[:120].replace(chr(10), ' ')}",
                        impact=rule["impact"],
                        fix=rule["fix"],
                        subject=f"{path}:{line}",
                        source="static",
                        cwe=rule.get("cwe", []),
                        tags=["iac"],
                        false_positive=rule.get("false_positive", ""),
                    )
                )
    # Absence checks per directory.
    dirs = {os.path.dirname(path) for path, _ in kinds["k8s"]}
    for directory in dirs:
        joined = "\n".join(text for path, text in kinds["k8s"] if os.path.dirname(path) == directory)
        if "kind: NetworkPolicy" not in joined:
            report.add(
                Finding(
                    check="infra.k8s.no-network-policy",
                    title="No NetworkPolicy in this manifest set",
                    severity="medium",
                    confidence="medium",
                    evidence=f"{directory}: no kind NetworkPolicy",
                    impact="Every pod can reach every pod by default.",
                    fix="Add a default deny policy and allow only required flows.",
                    subject=directory,
                    source="static",
                    cwe=["CWE-284"],
                    tags=["iac", "k8s"],
                    false_positive="A CNI without policy support or a policy in another directory.",
                )
            )
        if "pod-security.kubernetes.io" not in joined:
            report.add(
                Finding(
                    check="infra.k8s.no-pod-security",
                    title="No pod security label",
                    severity="low",
                    confidence="low",
                    evidence=f"{directory}: no pod-security label",
                    impact="Namespace enforcement is unclear.",
                    fix="Set restricted or baseline labels.",
                    subject=directory,
                    source="static",
                    cwe=["CWE-284"],
                    tags=["iac", "k8s"],
                    false_positive="A cluster policy applied outside the repo.",
                )
            )
    for path, text in kinds["docker"]:
        if not re.search(r"^\s*USER\s+(?!root)\S+", text, re.M):
            report.add(
                Finding(
                    check="infra.docker.no-user",
                    title="Container has no non-root USER",
                    severity="low",
                    confidence="medium",
                    evidence=path,
                    impact="The process runs as root by default.",
                    fix="Add a low privilege USER.",
                    subject=path,
                    source="static",
                    cwe=["CWE-250"],
                    tags=["iac", "docker"],
                )
            )
    for path, text in kinds["terraform"]:
        if "backend" not in text:
            report.add(
                Finding(
                    check="infra.tf.no-backend",
                    title="Terraform has no remote backend",
                    severity="low",
                    confidence="low",
                    evidence=path,
                    impact="State lives locally and is easy to lose.",
                    fix="Use a locked remote backend.",
                    subject=path,
                    source="static",
                    cwe=["CWE-693"],
                    tags=["iac", "terraform"],
                    false_positive="A module without its own state.",
                )
            )
        if "required_providers" not in text:
            report.add(
                Finding(
                    check="infra.tf.no-provider-pin",
                    title="Provider version not pinned",
                    severity="low",
                    confidence="medium",
                    evidence=path,
                    impact="A provider update can change behavior.",
                    fix="Pin provider versions.",
                    subject=path,
                    source="static",
                    cwe=["CWE-1104"],
                    tags=["iac", "terraform"],
                )
            )
    report.meta = {
        "files": len(files),
        "terraform": len(kinds["terraform"]),
        "k8s": len(kinds["k8s"]),
        "docker": len(kinds["docker"]),
        "cfn": len(kinds["cfn"]),
    }
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--profile", default="engineer", choices=("engineer", "bugbounty", "smb", "maintainer", "cra"))
    ap.add_argument("--fail-on", default="none", choices=("none", "info", "low", "medium", "high", "critical"))
    ap.add_argument("--baseline", default="")
    ap.add_argument("--suppress", default="", help="JSON Lines ignore file")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    report = scan(args.target)
    if args.suppress:
        suppress.apply_file(report, args.suppress)
    if args.baseline:
        report.suppress(load_report(args.baseline))
    print(report.to_json() if args.json else report_render.render_markdown(report, args.profile))
    if args.out:
        report.write_json(args.out + ".json")
        with open(args.out + ".md", "w", encoding="utf-8") as handle:
            handle.write(report_render.render_markdown(report, args.profile) + "\n")
    if args.fail_on != "none":
        raise SystemExit(report.exit_code(args.fail_on))


if __name__ == "__main__":
    main()
