#!/usr/bin/env python3
"""Finding and report model shared by every Beril scanner.

The model exists so that a header check, a secret hit, a JAR string and a
crash triage all speak the same language: severity, confidence, evidence,
impact, fix, scope and an honesty statement. Renderers live in
``report_render.py``; scanners must never print their own format.

Design rules
------------
1. A finding without evidence is a lead. Keep it, but never call it verified.
2. Confidence is about the detection, not the impact. A missing header is high
   confidence and low severity. A generic regex secret is low confidence.
3. Every report states what was checked and what was not.
4. IDs are deterministic so reruns and dedupe are stable.
5. The report never stores a full secret unless the caller asks for it.

    from beril_model import Finding, Report
    report = Report(target="https://example.com", mode="passive")
    report.add(Finding(check="web.header.hsts", ...))
    print(report.to_json())
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from dataclasses import dataclass, field

SCHEMA = "beril.report/1"
TOOL_VERSION = "1.4.0"

SEVERITIES = ("critical", "high", "medium", "low", "info")
CONFIDENCES = ("high", "medium", "low")
STATES = ("observed", "inferred")
SOURCES = ("passive", "active", "static", "history", "dependency", "triage", "tool")
MODES = ("passive", "active", "artifact", "source", "hunt", "jar", "mcp")
PROFILES = ("engineer", "bugbounty", "smb", "maintainer")

SEVERITY_WEIGHT = {"critical": 100, "high": 60, "medium": 30, "low": 10, "info": 2}
CONFIDENCE_FACTOR = {"high": 1.0, "medium": 0.7, "low": 0.4}
SEVERITY_EN = {
    "critical": "critical",
    "high": "high",
    "medium": "medium",
    "low": "low",
    "info": "info",
}
CONFIDENCE_EN = {"high": "high", "medium": "medium", "low": "low"}

SEVERITY_HELP = {
    "critical": "Fix today. Loss of data, money or full control.",
    "high": "Fix this week. Serious impact in one step.",
    "medium": "Plan it. A gap that weakens the defence.",
    "low": "Queue it. Hygiene and hardening.",
    "info": "For a decision. Not a risk on its own.",
}

CVSS_HINT = {
    "critical": (9.0, 10.0),
    "high": (7.0, 8.9),
    "medium": (4.0, 6.9),
    "low": (0.1, 3.9),
    "info": (0.0, 0.0),
}


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).isoformat(timespec="seconds")


def norm_subject(subject: str) -> str:
    """Normalize a subject so the same issue dedupes across runs."""
    value = subject.strip().lower()
    value = re.sub(r"https?://", "", value)
    value = re.sub(r":\d+", "", value)
    value = re.sub(r"/+", "/", value)
    return value[:200]


def finding_id(check: str, subject: str, evidence: str = "") -> str:
    raw = f"{check}|{norm_subject(subject)}|{evidence[:120]}"
    return hashlib.sha1(raw.encode("utf-8", "replace")).hexdigest()[:12]


def cvss_band(score: float | None) -> str:
    if score is None:
        return ""
    if score >= 9.0:
        return "critical"
    if score >= 7.0:
        return "high"
    if score >= 4.0:
        return "medium"
    if score > 0:
        return "low"
    return "info"


@dataclass
class Finding:
    check: str
    title: str
    severity: str
    confidence: str
    evidence: str
    impact: str
    fix: str
    subject: str = ""
    source: str = "passive"
    state: str = "observed"
    cwe: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    request: str = ""
    response: str = ""
    false_positive: str = ""
    verified: bool = False
    cvss_score: float | None = None
    cvss_vector: str = ""
    refs: list[str] = field(default_factory=list)
    kev: bool = False
    epss: float | None = None
    id: str = ""

    def __post_init__(self) -> None:
        self.severity = self.severity if self.severity in SEVERITIES else "info"
        self.confidence = self.confidence if self.confidence in CONFIDENCES else "low"
        self.source = self.source if self.source in SOURCES else "passive"
        self.state = self.state if self.state in STATES else "observed"
        if not self.subject:
            self.subject = self.evidence.split(":", 1)[0][:200] or self.check
        if not self.id:
            self.id = finding_id(self.check, self.subject)
        if self.state == "inferred" and self.confidence == "high":
            self.confidence = "medium"

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "check": self.check,
            "title": self.title,
            "severity": self.severity,
            "confidence": self.confidence,
            "state": self.state,
            "verified": bool(self.verified),
            "source": self.source,
            "subject": self.subject,
            "evidence": self.evidence,
            "impact": self.impact,
            "fix": self.fix,
            "false_positive": self.false_positive,
            "cwe": list(self.cwe),
            "tags": list(self.tags),
            "request": self.request,
            "response": self.response,
            "cvss_score": self.cvss_score,
            "cvss_vector": self.cvss_vector,
            "refs": list(self.refs),
            "kev": bool(self.kev),
            "epss": self.epss,
            "priority": self.priority(),
            "priority_reason": self.priority_reason(),
        }
        return data

    @classmethod
    def from_dict(cls, data: dict) -> Finding:
        known = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        return cls(**known)

    def priority(self) -> int:
        base = SEVERITY_WEIGHT[self.severity]
        factor = CONFIDENCE_FACTOR[self.confidence]
        multiplier = 1.0
        if self.verified:
            multiplier *= 1.2
        if self.source == "active":
            multiplier *= 1.1
        if self.kev:
            multiplier *= 1.5
        if self.epss:
            multiplier *= 1.0 + min(max(self.epss, 0.0), 1.0) * 0.8
        return round(base * factor * multiplier)

    def priority_reason(self) -> str:
        parts = [f"base {self.severity}", f"confidence {self.confidence}"]
        if self.verified:
            parts.append("verified")
        if self.kev:
            parts.append("in KEV")
        if self.epss is not None:
            parts.append(f"EPSS {self.epss:.3f}")
        return ", ".join(parts)

    def fingerprint(self) -> str:
        return f"{self.check}|{norm_subject(self.subject)}"


@dataclass
class Report:
    target: str
    mode: str = "passive"
    profile: str = "engineer"
    findings: list[Finding] = field(default_factory=list)
    started_at: str = field(default_factory=utc_now)
    finished_at: str = ""
    authorization: dict = field(default_factory=dict)
    scope: dict = field(default_factory=lambda: {"in_scope": [], "out_of_scope": [], "checked": [], "not_checked": []})
    limits: dict = field(default_factory=dict)
    meta: dict = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    schema: str = SCHEMA
    tool_version: str = TOOL_VERSION

    def __post_init__(self) -> None:
        if self.mode not in MODES:
            self.mode = "passive"
        if self.profile not in PROFILES:
            self.profile = "engineer"

    def add(self, finding: Finding) -> Finding | None:
        """Add with dedupe. Returns the stored finding, or None if out of scope."""
        fp = finding.fingerprint()
        for existing in self.findings:
            if existing.fingerprint() == fp:
                if CONFIDENCES.index(finding.confidence) < CONFIDENCES.index(existing.confidence):
                    existing.confidence = finding.confidence
                if finding.verified:
                    existing.verified = True
                if finding.evidence and finding.evidence not in existing.evidence:
                    existing.evidence = (existing.evidence + " | " + finding.evidence)[:2000]
                if finding.priority() > existing.priority():
                    existing.severity = finding.severity
                existing.kev = existing.kev or finding.kev
                if finding.epss is not None:
                    existing.epss = max(existing.epss or 0.0, finding.epss)
                return existing
        self.findings.append(finding)
        return finding

    def finish(self) -> Report:
        self.finished_at = utc_now()
        self.findings.sort(key=lambda x: (x.priority(), x.severity), reverse=True)
        return self

    def counts(self) -> dict:
        return {s: sum(1 for f in self.findings if f.severity == s) for s in SEVERITIES}

    def suppress(self, baseline: Report) -> int:
        """Drop findings already present in a baseline report.

        Matching is by id first, then by check and normalized subject. The
        count is recorded in meta so the renderer can state it.

        Args:
            baseline: Earlier report from the same target.

        Returns:
            Number of suppressed findings.
        """
        ids = {finding.id for finding in baseline.findings}
        fingerprints = {finding.fingerprint() for finding in baseline.findings}
        kept = [f for f in self.findings if f.id not in ids and f.fingerprint() not in fingerprints]
        removed = len(self.findings) - len(kept)
        self.findings = kept
        if removed:
            self.meta["suppressed"] = removed
        return removed

    def exit_code(self, threshold: str = "none") -> int:
        """Return a CI exit code for a severity threshold.

        Args:
            threshold: ``none``, ``info``, ``low``, ``medium``, ``high`` or ``critical``.

        Returns:
            1 when a finding is at or above the threshold, otherwise 0.
        """
        if threshold == "none":
            return 0
        rank = {severity: index for index, severity in enumerate(SEVERITIES)}
        limit = rank.get(threshold, len(SEVERITIES) - 1)
        return 1 if any(rank[f.severity] <= limit for f in self.findings) else 0

    def problems(self) -> list[str]:
        out = []
        required = ("check", "title", "evidence", "impact", "fix")
        for finding in self.findings:
            for name in required:
                if not str(getattr(finding, name, "")).strip():
                    out.append(f"{finding.id}: missing {name}")
            if finding.severity not in SEVERITIES:
                out.append(f"{finding.id}: bad severity")
            if finding.confidence not in CONFIDENCES:
                out.append(f"{finding.id}: bad confidence")
        return out

    def score(self) -> int:
        return sum(f.priority() for f in self.findings)

    def top_actions(self, limit: int = 5) -> list[Finding]:
        eligible = [
            f
            for f in self.findings
            if f.severity in ("critical", "high", "medium") and f.confidence in ("high", "medium")
        ]
        return sorted(eligible, key=lambda f: f.priority(), reverse=True)[:limit]

    def checked(self) -> list[str]:
        return list(self.scope.get("checked", []))

    def not_checked(self) -> list[str]:
        return list(self.scope.get("not_checked", []))

    def summary_line(self) -> str:
        c = self.counts()
        return f"{c['critical']} critical, {c['high']} high, {c['medium']} medium, {c['low']} low, {c['info']} info"

    def to_dict(self) -> dict:
        return {
            "schema": self.schema,
            "tool_version": self.tool_version,
            "target": self.target,
            "mode": self.mode,
            "profile": self.profile,
            "started_at": self.started_at,
            "finished_at": self.finished_at or utc_now(),
            "authorization": self.authorization,
            "scope": self.scope,
            "limits": self.limits,
            "meta": self.meta,
            "errors": self.errors,
            "counts": self.counts(),
            "score": self.score(),
            "top_actions": [f.id for f in self.top_actions()],
            "findings": [f.to_dict() for f in self.findings],
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def write_json(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(self.to_json() + "\n")


def report_from_dict(data: dict) -> Report:
    report = Report(
        target=data.get("target", ""),
        mode=data.get("mode", "passive"),
        profile=data.get("profile", "engineer"),
        started_at=data.get("started_at", ""),
        finished_at=data.get("finished_at", ""),
        authorization=data.get("authorization", {}),
        scope=data.get("scope", {}),
        limits=data.get("limits", {}),
        meta=data.get("meta", {}),
        errors=data.get("errors", []),
    )
    for item in data.get("findings", []):
        report.findings.append(Finding.from_dict(item))
    return report


def load_report(path: str) -> Report:
    with open(path, encoding="utf-8") as fh:
        return report_from_dict(json.load(fh))


def validate_finding_dict(data: dict) -> list[str]:
    problems = []
    for key in ("check", "title", "severity", "confidence", "evidence", "impact", "fix"):
        if not str(data.get(key, "")).strip():
            problems.append(f"missing {key}")
    if data.get("severity") not in SEVERITIES:
        problems.append("bad severity")
    if data.get("confidence") not in CONFIDENCES:
        problems.append("bad confidence")
    if data.get("state", "observed") not in STATES:
        problems.append("bad state")
    return problems
