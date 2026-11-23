#!/usr/bin/env python3
"""Open source project health check from a local clone.

Not a security scan and not a popularity score. It reads git history, the file
tree and the dependency inventory, then reports maintenance, release, test,
process and dependency signals with a reason for each.

    ./beril health --target ./repo
    ./beril health --target ./repo --json
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deps
import report_render
import sbom
import suppress
from beril_model import Finding, Report, load_report

SKIP = deps.SKIP | {".github/ISSUE_TEMPLATE"}
DIMENSIONS = ("maintenance", "release", "tests", "process", "dependencies", "docs")
MAX_FILES = 5_000


def git(root: str, *args: str) -> str:
    try:
        proc = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, timeout=30, errors="replace")
        return proc.stdout if proc.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def is_repo(root: str) -> bool:
    return bool(git(root, "rev-parse", "--is-inside-work-tree").strip())


def files(root: str) -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in filenames:
            out.append(os.path.relpath(os.path.join(dirpath, name), root))
            if len(out) >= MAX_FILES:
                return out
    return out


def commits_last_year(root: str) -> tuple[int, int, float]:
    log = git(root, "log", "--since=1.year", "--format=%ae")
    authors = [line.strip().lower() for line in log.splitlines() if line.strip()]
    if not authors:
        return 0, 0, 0.0
    counts: dict[str, int] = {}
    for author in authors:
        counts[author] = counts.get(author, 0) + 1
    top = max(counts.values())
    return len(authors), len(counts), round(top / len(authors), 2)


def releases_last_year(root: str) -> int:
    out = git(root, "for-each-ref", "--sort=-creatordate", "--format=%(refname:short) %(creatordate:unix)", "refs/tags")
    cutoff = dt.datetime.now().timestamp() - 365 * 86400
    count = 0
    for line in out.splitlines():
        parts = line.rsplit(" ", 1)
        if len(parts) == 2 and parts[1].isdigit() and int(parts[1]) >= cutoff:
            count += 1
    return count


def signed_tags(root: str) -> bool:
    return "BEGIN PGP SIGNATURE" in git(root, "tag", "-n99", "--format=%(contents)")


def score(value: int, full: int) -> int:
    return max(0, min(100, round(value / full * 100)))


def inspect(root: str) -> tuple[Report, dict]:
    report = Report(target=root, mode="source", profile="health")
    report.scope["checked"] = [
        "Commit activity in the last year",
        "Author spread",
        "Tag cadence",
        "Test, CI and security files",
        "Licence declaration",
        "Dependency inventory",
        "README and docs",
    ]
    report.scope["not_checked"] = [
        "Issue and pull request backlog (needs a forge API)",
        "Code review quality",
        "Downstream usage",
        "Maintainer availability",
        "Release artifact signatures",
    ]
    if not os.path.isdir(root):
        report.errors.append("target must be a directory")
        return report, {}
    tree = files(root)
    lower = [name.lower() for name in tree]
    has_tests = any(name.startswith(("tests/", "test/")) for name in lower) or any(
        name.endswith(("pytest.ini", "tox.ini", "conftest.py")) for name in lower
    )
    has_ci = any(name.startswith(".github/workflows/") for name in lower) or any(
        name in (".gitlab-ci.yml", ".circleci/config.yml", "azure-pipelines.yml") for name in lower
    )
    has_security = any(os.path.basename(name) in ("security.md", "security.txt") for name in lower)
    license_value = sbom.declared_license(root)
    readme = next((name for name in tree if os.path.basename(name).lower().startswith("readme")), "")
    docs_count = sum(1 for name in lower if name.startswith("docs/"))
    lockfile = any(
        os.path.basename(name)
        in ("package-lock.json", "poetry.lock", "cargo.lock", "go.sum", "pnpm-lock.yaml", "uv.lock")
        for name in lower
    )
    components = deps.collect(root)
    authors, author_count, top_share = commits_last_year(root) if is_repo(root) else (0, 0, 0.0)
    tags = releases_last_year(root) if is_repo(root) else 0
    signed = signed_tags(root) if is_repo(root) else False
    readme_size = 0
    if readme:
        try:
            readme_size = os.path.getsize(os.path.join(root, readme))
        except OSError:
            pass
    scores = {
        "maintenance": round(
            (score(authors, 200) + score(author_count, 5) + score(round((1 - top_share) * 100), 70)) / 3
        ),
        "release": round((score(tags, 6) + (20 if signed else 0)) * 100 / 120),
        "tests": 100 if has_tests and has_ci else 60 if has_tests else 20 if has_ci else 0,
        "process": (50 if has_security else 0) + (50 if license_value else 0),
        "dependencies": 100 if components and lockfile else 70 if lockfile else 40 if not components else 30,
        "docs": 100 if docs_count >= 5 else 70 if readme_size > 4000 else 50 if readme_size else 10,
    }
    report.meta["scorecard"] = scores
    report.meta["signals"] = {
        "commits_last_year": authors,
        "authors_last_year": author_count,
        "top_author_share": top_share,
        "releases_last_year": tags,
        "signed_tags": signed,
        "tests": has_tests,
        "ci": has_ci,
        "security_file": has_security,
        "license": license_value,
        "lockfile": lockfile,
        "direct_components": len(components),
        "files": len(tree),
    }

    def add(
        check: str,
        title: str,
        severity: str,
        evidence: str,
        impact: str,
        fix: str,
        confidence: str = "high",
        cwe: list[str] | None = None,
    ) -> None:
        report.add(
            Finding(
                check="health." + check,
                title=title,
                severity=severity,
                confidence=confidence,
                evidence=evidence,
                impact=impact,
                fix=fix,
                subject=root,
                source="static",
                tags=["health"],
                cwe=cwe or [],
            )
        )

    if not has_tests:
        add(
            "no-tests",
            "No test directory or test runner config",
            "high",
            f"{root}: no tests/",
            "A change cannot be checked before release.",
            "Add a regression suite and run it in CI.",
        )
    if not has_ci:
        add(
            "no-ci",
            "No CI configuration",
            "medium",
            f"{root}: no workflow file",
            "Checks depend on the author remembering.",
            "Add a workflow that runs the test suite.",
        )
    if not has_security:
        add(
            "no-security-file",
            "No SECURITY.md",
            "medium",
            f"{root}: no SECURITY.md",
            "A reporter does not know where to send a bug.",
            "Add SECURITY.md with a private channel and a window.",
        )
    if not license_value:
        add(
            "no-license",
            "No licence file",
            "medium",
            f"{root}: no LICENSE",
            "Reuse is legally unclear.",
            "Add an OSI licence.",
        )
    if is_repo(root) and authors == 0:
        add(
            "stale",
            "No commit in the last year",
            "medium",
            f"{root}: git log --since=1.year is empty",
            "Fixes may not arrive.",
            "Confirm the maintenance status or fork.",
        )
    if author_count == 1 and authors > 20:
        add(
            "bus-factor",
            "One author wrote every recent commit",
            "medium",
            f"{root}: 1 author, {authors} commits",
            "Illness or loss of interest stops the project.",
            "Add a second maintainer with merge rights.",
            "high",
        )
    if not lockfile and components:
        add(
            "no-lockfile",
            "Dependencies without a lockfile",
            "low",
            f"{root}: {len(components)} components, no lock",
            "Two installs can resolve different versions.",
            "Commit a lockfile.",
        )
    if len(components) > 500:
        add(
            "dependency-load",
            "Large direct dependency count",
            "low",
            f"{root}: {len(components)} components",
            "Every upgrade is a review cost.",
            "Remove unused packages and group updates.",
        )
    if not signed:
        add(
            "unsigned-tags",
            "No signed release tags",
            "low",
            f"{root}: no PGP signature in tags",
            "A tag can be moved without evidence.",
            "Sign release tags.",
            "medium",
        )
    report.finish()
    return report, scores


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--baseline", default="")
    ap.add_argument("--suppress", default="")
    args = ap.parse_args()
    report, _scores = inspect(args.target)
    if args.suppress:
        suppress.apply_file(report, args.suppress)
    if args.baseline:
        report.suppress(load_report(args.baseline))
    print(report.to_json() if args.json else report_render.render_markdown(report, "health"))
    if args.out:
        report.write_json(args.out + ".json")
        with open(args.out + ".md", "w", encoding="utf-8") as handle:
            handle.write(report_render.render_markdown(report, "health") + "\n")
    raise SystemExit(0 if report.meta.get("scorecard") else 1)


if __name__ == "__main__":
    main()
