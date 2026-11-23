#!/usr/bin/env python3
"""Container image scan through Trivy, Grype and Syft.

The image is referenced by name or by a saved tar. Tools must be installed. The
SBOM is written next to the report when Syft exists.

    ./beril image --target alpine:3.20
    ./beril image --target ./app.tar --only trivy --out scans/app-image
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adapters
import report_render
from beril_model import Finding, Report

TOOLS = ("trivy", "grype", "syft")


def run(args: list[str], timeout: int = 600) -> tuple[str, str, int]:
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=timeout, errors="replace")
        return proc.stdout[:8_000_000], proc.stderr[:10_000], proc.returncode
    except Exception as exc:
        return "", f"{type(exc).__name__}: {exc}", 1


def scan(target: str, tools: list[str], offline: bool, out: str) -> Report:
    report = Report(target=target, mode="artifact")
    report.scope["checked"] = [f"Adapter: {name}" for name in tools]
    report.scope["not_checked"] = ["Runtime behavior", "Image signature and provenance", "Base image freshness policy"]
    report.limits = {"tools": tools, "network": "off" if offline else "on"}
    if out:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    for name in tools:
        if not adapters.AVAILABLE.get(name):
            report.errors.append(f"{name} not installed")
            continue
        if name == "trivy":
            args = ["trivy", "image", "--format", "json", "--scanners", "vuln,secret", "--quiet"]
            if offline:
                args.append("--offline-scan")
            args.append(target)
            stdout, stderr, code = run(args)
            findings = adapters.parse_trivy(stdout)
        elif name == "grype":
            stdout, stderr, code = run(["grype", target, "-o", "json", "-q"])
            findings = adapters.parse_grype(stdout)
        else:
            sbom_path = (out or "scans/image") + ".cdx.json"
            os.makedirs(os.path.dirname(os.path.abspath(sbom_path)), exist_ok=True)
            stdout, stderr, code = run(["syft", target, "-o", "cyclonedx-json", "-q"])
            findings = []
            if stdout.strip():
                with open(sbom_path, "w", encoding="utf-8") as handle:
                    handle.write(stdout)
                report.meta["sbom"] = sbom_path
                findings = [
                    Finding(
                        check="image.sbom",
                        title="SBOM written",
                        severity="info",
                        confidence="high",
                        evidence=sbom_path,
                        impact="Component inventory for review.",
                        fix="Keep it with the image digest.",
                        subject=sbom_path,
                        source="tool",
                    )
                ]
        if code not in (0, 1) and not findings:
            report.errors.append(f"{name}: exit {code} {stderr[:200]}")
            continue
        for finding in findings:
            report.add(finding)
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--only", default="")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--out", default="")
    ap.add_argument("--fail-on", default="none", choices=("none", "info", "low", "medium", "high", "critical"))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    tools = [x.strip() for x in args.only.split(",") if x.strip()] or list(TOOLS)
    report = scan(args.target, tools, args.offline, args.out)
    print(report.to_json() if args.json else report_render.render_markdown(report, "engineer"))
    if args.out:
        report.write_json(args.out + ".json")
        with open(args.out + ".md", "w", encoding="utf-8") as handle:
            handle.write(report_render.render_markdown(report, "engineer") + "\n")
    if args.fail_on != "none":
        raise SystemExit(report.exit_code(args.fail_on))


if __name__ == "__main__":
    main()
