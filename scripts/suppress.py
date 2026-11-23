#!/usr/bin/env python3
"""Apply a reviewed ignore file to a report.

Each line is a JSON object:

    {"check": "infra.tf-public-acl", "subject": "examples/*", "reason": "demo bucket", "expires": "2027-01-01"}

``check`` is a glob, ``subject`` an optional glob, ``id`` an exact fingerprint.
A rule without a reason is still applied and counted. Expired rules do not
match. The file is reviewed like code.

    from suppress import apply_file
    removed = apply_file(report, ".berilignore")
"""

from __future__ import annotations

import datetime as dt
import fnmatch
import json
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from beril_model import Finding, Report

IGNORE_NAME = ".berilignore"


def load(path: str) -> list[dict]:
    """Read rules from a JSON Lines file.

    Args:
        path: Ignore file.

    Returns:
        Rule dicts, malformed lines skipped.
    """
    rules = []
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            for line in handle:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    rule = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(rule, dict):
                    rules.append(rule)
    except OSError:
        return []
    return rules


def expired(rule: dict, today: dt.date | None = None) -> bool:
    """True when a rule has an ``expires`` date in the past."""
    value = str(rule.get("expires", "")[:10])
    if not value:
        return False
    try:
        return dt.date.fromisoformat(value) < (today or dt.date.today())
    except ValueError:
        return False


def matches(rule: dict, finding: Finding) -> bool:
    """True when a rule applies to a finding.

    Args:
        rule: One ignore rule.
        finding: Finding object.

    Returns:
        Match result.
    """
    if expired(rule):
        return False
    if rule.get("id") and rule["id"] == finding.id:
        return True
    check = str(rule.get("check", ""))
    if not check or not fnmatch.fnmatch(finding.check, check):
        return False
    subject = str(rule.get("subject", ""))
    if subject and not fnmatch.fnmatch(finding.subject, subject):
        return False
    tag = str(rule.get("tag", ""))
    return not (tag and tag not in finding.tags)


def apply_rules(report: Report, rules: list[dict]) -> int:
    """Remove matching findings and record the count.

    Args:
        report: Report object.
        rules: Ignore rules.

    Returns:
        Removed count.
    """
    kept = [finding for finding in report.findings if not any(matches(rule, finding) for rule in rules)]
    removed = len(report.findings) - len(kept)
    report.findings = kept
    if removed:
        report.meta["suppressed"] = int(report.meta.get("suppressed", 0)) + removed
    return removed


def apply_file(report: Report, path: str = IGNORE_NAME) -> int:
    """Load and apply an ignore file when it exists."""
    if not path or not os.path.isfile(path):
        return 0
    report.meta["suppressed_by"] = path
    return apply_rules(report, load(path))
