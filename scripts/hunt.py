#!/usr/bin/env python3
"""Bug hunt loop for an open source repository, local and sandboxed.

Phases mirror the research loop: fingerprint, known CVE mapping, source rules,
git history, structural risk, then an optional sandbox build with sanitizers.
Only signature-backed crashes become "reproduced". Everything else stays a
candidate with a line number.

The report targets a maintainer, not a customer. It says AI assisted and keeps
the smallest reproduction.

    python scripts/hunt.py --target ./repo
    python scripts/hunt.py --target ./repo --sandbox --report HUNT.md
    python scripts/hunt.py --target ./repo --fuzz --timebox 900
"""

from __future__ import annotations

import argparse
import collections
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deps
import fileio
import report_render
import source_audit
import triage_crash
from beril_model import Finding, Report

SKIP = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    "dist",
    "build",
    "target",
    ".next",
    "coverage",
    "vendor",
}
LANG_BY_EXT = {
    ".py": "python",
    ".js": "node",
    ".ts": "node",
    ".go": "go",
    ".rs": "rust",
    ".c": "c",
    ".h": "c",
    ".cpp": "c",
}
BUILD_FILES = {
    "pyproject.toml": "python",
    "requirements.txt": "python",
    "setup.py": "python",
    "package.json": "node",
    "go.mod": "go",
    "Cargo.toml": "rust",
    "CMakeLists.txt": "c",
    "Makefile": "c",
}
SECURITY_WORDS = re.compile(
    r"(?i)\b(fix|security|vuln|cve|xss|sqli|rce|overflow|uaf|race|sanitiz|" r"escape|traversal|ssrf|deserial|bypass)\b"
)


def run(cmd: list[str], cwd: str, timeout: int = 30) -> str:
    try:
        out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, errors="replace")
        return (out.stdout or "") + (out.stderr or "")
    except Exception as exc:
        return f"{type(exc).__name__}: {exc}"


def fingerprint(root: str) -> dict:
    files, langs, sizes = 0, collections.Counter(), 0
    tests, ci, security_md = 0, [], False
    stop = False
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in filenames:
            path = os.path.join(dirpath, name)
            try:
                sizes += os.path.getsize(path)
            except OSError:
                pass
            files += 1
            lang = LANG_BY_EXT.get(os.path.splitext(name)[1].lower())
            if lang:
                langs[lang] += 1
            if name in ("SECURITY.md", ".security.md"):
                security_md = True
            if "test" in name.lower() or "spec" in name.lower():
                tests += 1
            if ".github/workflows" in path.replace(os.sep, "/") or name in (".gitlab-ci.yml", "Jenkinsfile"):
                ci.append(os.path.relpath(path, root))
            if files >= 60_000:
                stop = True
                break
        if stop:
            break
    git = os.path.isdir(os.path.join(root, ".git"))
    commits = []
    if git:
        log = run(
            ["git", "log", "--no-merges", "-n", "300", "--pretty=%h%C0%x09%ad%C0%x09%s", "--date=short"], root, 60
        )
        commits = [line for line in log.splitlines() if line.count("\t") >= 2]
    return {
        "files": files,
        "languages": dict(langs),
        "bytes": sizes,
        "tests": tests,
        "ci": ci[:20],
        "security_md": security_md,
        "git": git,
        "commits": commits,
    }


def history_findings(root: str, commits: list[str]) -> list[Finding]:
    out = []
    security = [c for c in commits if SECURITY_WORDS.search(c.split("\t", 2)[-1])]
    for line in security[:8]:
        sha, date, subject = line.split("\t", 2)
        out.append(
            Finding(
                check="hunt.security-commit",
                title="Security-looking commit",
                severity="info",
                confidence="medium",
                evidence=f"{sha} {date}: {subject[:140]}",
                impact="A lead for reading the patch pattern and the silent fix.",
                fix="Read the diff and check whether the same bug exists elsewhere.",
                subject=f"git:{sha}",
                source="history",
                tags=["git"],
            )
        )
    if not security and commits:
        out.append(
            Finding(
                check="hunt.no-security-history",
                title="No security hint in recent commits",
                severity="info",
                confidence="low",
                evidence=f"scanned {len(commits)} commits",
                impact="No silent patch marker found.",
                fix="Read older history or the changelog.",
                subject=root,
                source="history",
            )
        )
    return out


def structure_findings(root: str, fp: dict) -> list[Finding]:
    out = []
    if not fp["security_md"]:
        out.append(
            Finding(
                check="hunt.no-security-policy",
                title="No SECURITY.md",
                severity="low",
                confidence="high",
                evidence=root,
                impact="The private reporting channel is unclear.",
                fix="Add SECURITY.md and enable GitHub private advisories.",
                subject=root,
                source="static",
            )
        )
    if fp["tests"] == 0:
        out.append(
            Finding(
                check="hunt.no-tests",
                title="No test file",
                severity="low",
                confidence="high",
                evidence=root,
                impact="Reproduction and regression are hard.",
                fix="Add at least one smoke test.",
                subject=root,
                source="static",
            )
        )
    for ci in fp["ci"]:
        text = ""
        try:
            text = fileio.read_text(os.path.join(root, ci))
        except OSError:
            pass
        if "pull_request_target" in text:
            out.append(
                Finding(
                    check="hunt.ci-pr-target",
                    title="pull_request_target in use",
                    severity="medium",
                    confidence="medium",
                    evidence=ci,
                    impact="PR code can run with secrets.",
                    fix="Narrow the permissions and pin the checkout ref.",
                    subject=ci,
                    source="static",
                    cwe=["CWE-829"],
                    tags=["ci"],
                )
            )
    return out


def fuzz_suggestion(root: str, langs: dict) -> str:
    top = max(langs, key=lambda name: langs[name]) if langs else ""
    lines = ["## Fuzz suggestion", ""]
    if top == "c":
        lines += [
            "```bash",
            "cc -g -O1 -fsanitize=address,undefined,fuzzer harness.c -o fuzz",
            "./fuzz -max_total_time=300 corpus/",
            "```",
        ]
    elif top == "python":
        lines += [
            "```bash",
            "python -m pip install atheris",
            "python fuzz_harness.py -max_total_time=300",
            "```",
            "",
            "A harness skeleton is in `scripts/afl_harness.c` and `references/fuzzing.md`.",
        ]
    elif top == "go":
        lines += ["```bash", "go test -fuzz=FuzzParse -fuzztime=5m ./...", "```"]
    elif top == "rust":
        lines += ["```bash", "cargo fuzz init", "cargo fuzz run fuzz_target_1 -- -max_total_time=300", "```"]
    elif top == "node":
        lines += ["```bash", "npx jazzer fuzz.js corpus/ -- --sync", "```"]
    else:
        lines += ["Language unknown. Write a harness for the smallest parser."]
    lines += ["", "Rule: run without network in isolation, keep the crash input and dedupe by signature."]
    return "\n".join(lines)


def sandbox_run(root: str, lang: str, timebox: int) -> tuple[str, str]:
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sandbox.sh")
    if not os.path.isfile(script) or not shutil.which("docker"):
        return "", "docker or sandbox.sh missing"
    with tempfile.NamedTemporaryFile(prefix="beril-sandbox-", suffix=".log", delete=False) as tmp:
        log_path = tmp.name
    try:
        proc = subprocess.run(
            ["bash", script, "--target", root, "--lang", lang, "--timeout", str(timebox)],
            capture_output=True,
            text=True,
            timeout=timebox + 120,
            errors="replace",
        )
        log = (proc.stdout or "") + (proc.stderr or "")
    except Exception as exc:
        log = f"{type(exc).__name__}: {exc}"
    with open(log_path, "w", encoding="utf-8") as fh:
        fh.write(log)
    return log_path, log


def scan(target: str, timebox: int = 300, use_sandbox: bool = False, fuzz: bool = False) -> Report:
    report = Report(target=target, mode="hunt", profile="maintainer")
    report.scope["checked"] = [
        "Language and build system fingerprint",
        "Dependency and OSV seed match",
        "Source rules and fan-in",
        "Git history",
        "CI and security policy",
    ]
    report.scope["not_checked"] = [
        "Full call graph",
        "Dynamic behavior (when the sandbox is off)",
        "Third party services",
        "Business logic",
    ]
    fp = fingerprint(target)
    report.meta = {k: v for k, v in fp.items() if k != "commits"}
    report.meta["commits_scanned"] = len(fp["commits"])
    report.limits = {"timebox_seconds": timebox, "network": "off (sandbox)"}
    if fp["files"] == 0:
        report.errors.append("no source file")
        return report.finish()

    dep_report = deps.scan(target, online=False, do_reach=True)
    for finding in dep_report.findings:
        report.add(finding)
    texts = {}
    for dirpath, dirnames, filenames in os.walk(target):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in filenames:
            if len(texts) >= 5_000:
                break
            if os.path.splitext(name)[1].lower() in source_audit.LANG_BY_EXT:
                path = os.path.join(dirpath, name)
                try:
                    texts[os.path.relpath(path, target)] = fileio.read_text(path, 500_000)
                except OSError:
                    pass
        if len(texts) >= 5_000:
            break
    for rel, text in texts.items():
        for finding in source_audit.scan_text(rel, text, source_audit.lang_of(rel, rel)):
            report.add(finding)
    for finding in source_audit.fan_in(texts):
        report.add(finding)
    for finding in history_findings(target, fp["commits"]):
        report.add(finding)
    for finding in structure_findings(target, fp):
        report.add(finding)

    if use_sandbox:
        lang = max(fp["languages"], key=fp["languages"].get) if fp["languages"] else ""
        lang = "c" if lang == "c" else lang
        if not lang:
            report.errors.append("could not identify a language for the sandbox")
        else:
            log_path, log = sandbox_run(target, lang, timebox)
            report.meta["sandbox_log"] = log_path
            report.meta["sandbox_exit"] = "build output below" if log_path else log
            if log_path:
                for finding in triage_crash.triage(log, target, log_path):
                    report.add(finding)
                if not any(f.check.startswith("crash.") for f in report.findings):
                    report.errors.append("sandbox ran without a sanitizer signature. A build or test error is likely")

    if fuzz:
        report.meta["fuzz"] = fuzz_suggestion(target, fp["languages"])
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--sandbox", action="store_true")
    ap.add_argument("--fuzz", action="store_true")
    ap.add_argument("--timebox", type=int, default=300)
    ap.add_argument("--report", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    if not os.path.isdir(args.target):
        sys.exit("target must be a directory")
    report = scan(args.target, args.timebox, args.sandbox, args.fuzz)
    text = report.to_json() if args.json else report_render.render_maintainer(report)
    print(text)
    if args.report:
        with open(args.report, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    if args.out:
        report.write_json(args.out + ".json")
        with open(args.out + ".md", "w", encoding="utf-8") as fh:
            fh.write(report_render.render_maintainer(report) + "\n")


if __name__ == "__main__":
    main()
