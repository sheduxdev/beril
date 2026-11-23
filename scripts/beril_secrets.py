#!/usr/bin/env python3
"""Secret detection with masking, context and an optional live check.

Default behavior is local and read-only: patterns, context and entropy. The
value is masked in the report. ``--verify`` sends the key to the provider's
own read-only endpoint and needs explicit consent because it leaves the host.

Confidence is deliberately conservative:

- test, example, docs or fixture paths lower confidence;
- placeholder markers lower confidence;
- generic patterns never exceed low confidence;
- a successful provider check raises confidence and sets ``verified``.

    python scripts/beril_secrets.py --target ./repo --history
    python scripts/beril_secrets.py --target ./repo --verify --json
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import os
import re
import subprocess
import sys
import urllib.request
from collections.abc import Iterator
from pathlib import Path

import paths

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import suppress
from beril_model import Finding, Report

MAX_BYTES = 2_000_000
MAX_FILES = 20_000
MAX_HITS_PER_RULE = 40
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {
    ".git",
    ".svn",
    ".hg",
    "node_modules",
    "vendor",
    "dist",
    "build",
    "target",
    ".venv",
    "venv",
    "__pycache__",
    ".next",
    ".nuxt",
    "coverage",
    "raw",
    "evidence",
    "scans",
    "profile",
    ".idea",
    ".vscode-test",
}

TEXT_EXT = {
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".py",
    ".rb",
    ".php",
    ".java",
    ".kt",
    ".go",
    ".rs",
    ".c",
    ".h",
    ".cpp",
    ".hpp",
    ".cs",
    ".swift",
    ".m",
    ".mm",
    ".scala",
    ".sh",
    ".bash",
    ".zsh",
    ".ps1",
    ".yml",
    ".yaml",
    ".json",
    ".json5",
    ".toml",
    ".ini",
    ".cfg",
    ".conf",
    ".env",
    ".xml",
    ".html",
    ".vue",
    ".svelte",
    ".sql",
    ".md",
    ".txt",
    ".gradle",
    ".properties",
    ".tf",
    ".tfvars",
    ".dockerfile",
    ".plist",
    ".pem",
    ".key",
    ".kdbx",
}
SPECIAL_NAMES = {"Dockerfile", "Makefile", ".env", ".npmrc", ".pypirc", "config.json", "mcp.json"}

EXAMPLE_HINTS = ("example", "sample", "test", "spec", "fixture", "mock", "demo", "doc", "readme", ".md")
PLACEHOLDERS = re.compile(
    r"(?i)^(x{4,}|\.{3,}|<[^>]+>|\$\{[^}]+\}|changeme|change_me|your[_-]?\w+|placeholder|"
    r"dummy|fake|test|todo|redacted|none|null|0{6,}|123456|password)"
)

# (provider, severity, confidence, regex, group)
RULES = [
    ("aws", "critical", "high", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"), 0),
    ("aws", "high", "medium", re.compile(r"aws_secret_access_key\s*[:=]\s*['\"]?([A-Za-z0-9/+=]{40})", re.I), 1),
    ("github", "critical", "high", re.compile(r"\b(gh[pousr]_[A-Za-z0-9]{36,90})\b"), 1),
    ("github", "medium", "medium", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{22,90}\b"), 0),
    ("gitlab", "critical", "high", re.compile(r"\bglpat-[A-Za-z0-9_-]{20,}"), 0),
    ("google", "high", "high", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"), 0),
    ("openai", "critical", "high", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}"), 0),
    ("anthropic", "critical", "high", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}"), 0),
    ("deepseek", "high", "medium", re.compile(r"\bsk-[a-f0-9]{32}\b"), 0),
    ("huggingface", "high", "high", re.compile(r"\bhf_[A-Za-z0-9]{30,}"), 0),
    ("stripe", "critical", "high", re.compile(r"\b(?:sk|rk)_(?:live|test)_[0-9A-Za-z]{16,}"), 0),
    ("slack", "high", "high", re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{10,}"), 0),
    ("slack", "medium", "medium", re.compile(r"https://hooks\.slack\.com/services/[A-Za-z0-9/]{20,}"), 0),
    ("supabase", "high", "medium", re.compile(r"\beyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}"), 0),
    ("private-key", "critical", "high", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----"), 0),
    ("postgres", "high", "high", re.compile(r"\bpostgres(?:ql)?://[^\s'\"<>]+:[^\s'\"<>@]+@[^\s'\"<>]+"), 0),
    ("mongodb", "high", "high", re.compile(r"\bmongodb(?:\+srv)?://[^\s'\"<>]+:[^\s'\"<>@]+@[^\s'\"<>]+"), 0),
    ("redis", "high", "high", re.compile(r"\bredis://(?:[^\s'\"<>@]*):([^\s'\"<>@]+)@[^\s'\"<>]+"), 0),
    ("mysql", "high", "high", re.compile(r"\bmysql://[^\s'\"<>]+:[^\s'\"<>@]+@[^\s'\"<>]+"), 0),
    ("jwt", "info", "low", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}"), 0),
    ("npm", "critical", "high", re.compile(r"\bnpm_[A-Za-z0-9]{36}\b"), 0),
    ("pypi", "critical", "high", re.compile(r"\bpypi-AgEIcHlwaS5vcmc[A-Za-z0-9_-]{50,}"), 0),
    ("discord", "high", "high", re.compile(r"\b[MN][A-Za-z\d]{23}\.[\w-]{6}\.[\w-]{27}\b"), 0),
    ("sendgrid", "critical", "high", re.compile(r"\bSG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}\b"), 0),
    ("telegram", "high", "high", re.compile(r"\b\d{8,10}:AA[A-Za-z0-9_-]{33}\b"), 0),
    ("twilio", "high", "medium", re.compile(r"\bSK[0-9a-fA-F]{32}\b"), 0),
    ("shopify", "high", "high", re.compile(r"\bshpat_[0-9a-fA-F]{32}\b"), 0),
    ("notion", "high", "high", re.compile(r"\bsecret_[A-Za-z0-9]{43}\b"), 0),
    ("datadog", "high", "medium", re.compile(r"\b(?:ddapi|ddog|ddp)_[A-Za-z0-9]{20,}\b"), 0),
    (
        "generic",
        "medium",
        "low",
        re.compile(
            r"(?i)\b(?:api[_-]?key|apikey|secret|token|passwd|password|pwd|access[_-]?key)\b"
            r"\s*[:=]\s*['\"]([A-Za-z0-9_./+=-]{12,})['\"]"
        ),
        1,
    ),
    ("generic", "low", "low", re.compile(r"(?i)\b(?:api[_-]?key|secret|token)\b\s*[:=]\s*([A-Za-z0-9_./+=-]{16,})"), 1),
]

MCP_HINTS = ("mcp", "claude_desktop_config", ".cursor", ".vscode", ".claude")


def mask(value: str) -> str:
    value = value.strip()
    if len(value) <= 8:
        return value[:2] + "***"
    if len(value) <= 20:
        return value[:4] + "..." + value[-2:]
    return value[:4] + "..." + value[-4:]


def entropy(value: str) -> float:
    if not value:
        return 0.0
    counts = collections.Counter(value)
    total = len(value)
    return -sum((n / total) * math.log2(n / total) for n in counts.values())


def is_placeholder(value: str) -> bool:
    if PLACEHOLDERS.search(value):
        return True
    if set(value) <= set("xX*.-_0123456789"):
        return True
    if re.search(r"(?i)x{6,}", value):
        return True
    return bool(re.search(r"(.)\1{11,}", value))


def in_example_path(path: str) -> bool:
    low = path.lower()
    return any(hint in low for hint in EXAMPLE_HINTS)


_GUIDES: dict | None = None


def provider_guide(provider: str) -> dict:
    global _GUIDES
    if _GUIDES is None:
        try:
            with open(os.path.join(paths.DATA, "secret_providers.json"), encoding="utf-8") as fh:
                _GUIDES = json.load(fh).get("providers", {})
        except (OSError, json.JSONDecodeError):
            _GUIDES = {}
    return _GUIDES.get(provider, {})


def adjust(provider: str, severity: str, confidence: str, value: str, path: str) -> tuple[str, str, list[str], str]:
    tags, note = [], ""
    if in_example_path(path):
        confidence = "low" if confidence != "low" else "low"
        tags.append("example-path")
        note = "The path looks like an example, test or document."
    if is_placeholder(value):
        confidence = "low"
        severity = "info" if severity in ("critical", "high") else severity
        tags.append("placeholder")
        note = (note + " The value looks like a placeholder.").strip()
    if entropy(value) < 2.6 and provider not in ("private-key", "postgres", "mongodb", "mysql"):
        if confidence == "high":
            confidence = "medium"
        tags.append("low-entropy")
    if provider == "generic":
        confidence = "low"
    return severity, confidence, tags, note


def scan_text(name: str, text: str, limit_per_rule: int = MAX_HITS_PER_RULE) -> list[Finding]:
    findings: list[Finding] = []
    seen = collections.Counter()
    for provider, severity, confidence, pattern, group in RULES:
        for match in pattern.finditer(text):
            if seen[provider] >= limit_per_rule:
                break
            value = match.group(group) if match.groups() else match.group(0)
            if len(value) < 8:
                continue
            if provider == "generic" and entropy(value) < 3.0 and len(value) < 24:
                continue
            line = text[: match.start()].count("\n") + 1
            severity, confidence, tags, note = adjust(provider, severity, confidence, value, name)
            guide = provider_guide(provider)
            seen[provider] += 1
            finding = Finding(
                check=f"secret.{provider}",
                title=f"Possible {guide.get('name', provider)}",
                severity=severity,
                confidence=confidence,
                evidence=f"{name}:{line} {mask(value)} ({provider})",
                impact=(
                    "Key leak. If the value is live it allows API calls, data access "
                    "or resource use in the owner name."
                ),
                fix=f"Revoke first: {guide.get('revoke', 'provider console')}. Then issue a new key, "
                f"then clean git history. {guide.get('rotate', '')}".strip(),
                subject=f"{name}:{line}",
                source="static",
                cwe=["CWE-798"],
                false_positive=note or "Generic pattern match. The value may not be live.",
                refs=[guide.get("revoke", "")] if guide.get("revoke") else [],
                tags=[*tags, f"provider:{provider}"],
            )
            findings.append(finding)
    return findings


def scan_file(path: Path, findings: list[Finding]) -> None:
    try:
        if path.stat().st_size > MAX_BYTES:
            return
        raw = path.read_bytes()
        if b"\x00" in raw[:4096] and path.suffix.lower() not in TEXT_EXT:
            return
        text = raw.decode("utf-8", errors="replace")
    except OSError:
        return
    findings.extend(scan_text(str(path), text))


def iter_files(root: str) -> Iterator[Path]:
    if os.path.isfile(root):
        yield Path(root)
        return
    count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            path = Path(dirpath) / name
            if path.suffix.lower() not in TEXT_EXT and name not in SPECIAL_NAMES:
                continue
            yield path
            count += 1
            if count >= MAX_FILES:
                return


def scan_history(root: str, findings: list[Finding], max_commits: int = 300) -> None:
    if not (Path(root) / ".git").exists():
        return
    try:
        log = subprocess.run(
            ["git", "-C", root, "log", "--all", "--no-merges", f"-n{max_commits}", "-p", "-U0", "--", "."],
            capture_output=True,
            text=True,
            timeout=180,
            errors="replace",
        )
    except Exception:
        return
    current = ""
    for line in log.stdout.splitlines():
        if line.startswith(("+++ b/", "+++ ")):
            current = line.split("\t")[-1].replace("+++ b/", "").strip()
        elif line.startswith("+") and not line.startswith("+++") and current:
            for finding in scan_text(f"{current}@git", line[1:], limit_per_rule=3):
                finding.source = "history"
                finding.title = finding.title + " (git history)"
                finding.evidence = finding.evidence.replace("@git:", "@git:")
                findings.append(finding)


def verify(finding: Finding, secret: str, base: str = "") -> Finding:
    provider = finding.check.split(".", 1)[-1]
    guide = provider_guide(provider).get("verify", {})
    if guide.get("method") != "http":
        finding.false_positive = (finding.false_positive + " Live verification is not available for this type.").strip()
        return finding
    url = guide.get("url", "").replace("{secret}", secret)
    headers = {"User-Agent": "Beril/1.4 secret-check"}
    if guide.get("header"):
        headers[guide["header"]] = guide.get("prefix", "") + secret
    headers.update(guide.get("extra", {}))
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            status = resp.status
            resp.read(2048)
    except Exception as exc:
        status = getattr(exc, "code", 0)
        finding.evidence += f" [live check: {status or type(exc).__name__}]"
        if status in (401, 403):
            finding.confidence = "high"
            finding.false_positive = "The provider rejected the key. It may be revoked."
        return finding
    finding.evidence += f" [live check: HTTP {status}]"
    if 200 <= status < 300:
        finding.verified = True
        finding.confidence = "high"
        finding.false_positive = "The provider answered. Check the scope of the key separately."
    return finding


def build_report(target: str, history: bool = False, live: bool = False, max_files: int = MAX_FILES) -> Report:
    report = Report(target=target, mode="source", profile="engineer")
    findings: list[Finding] = []
    files = 0
    for path in iter_files(target):
        scan_file(path, findings)
        files += 1
        if files >= max_files:
            break
    if history:
        scan_history(target, findings)
    report.scope["checked"] = [f"{files} files, patterns and context", "Placeholder and example path filter"]
    if history:
        report.scope["checked"].append("Git history (last 300 commits, added lines)")
    report.scope["not_checked"] = [
        "Live verification off" if not live else "Providers verifiable over HTTP only",
        "Encrypted archives and keys inside binaries",
        "Cloud secret stores (Vault, SSM)",
    ]
    report.limits = {"max_files": max_files, "max_bytes_per_file": MAX_BYTES}
    for finding in findings:
        report.add(finding)
    report.meta["provider_guides"] = {
        f.check.split(".", 1)[-1]: provider_guide(f.check.split(".", 1)[-1]).get("revoke", "")
        for f in findings
        if f.check != "secret.generic"
    }
    if live:
        _live_pass(report)
    report.finish()
    return report


def _live_pass(report: Report) -> None:
    """Verify only findings whose raw value can be recovered from the mask."""

    # The mask is not enough. Rescan the tree cheaply and keep values in memory.
    values: dict[str, str] = {}
    root = report.target
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for provider, _sev, _conf, pattern, group in RULES:
            for match in pattern.finditer(text):
                value = match.group(group) if match.groups() else match.group(0)
                values.setdefault(provider, value)
                break
    for finding in report.findings:
        provider = finding.check.split(".", 1)[-1]
        if provider in values:
            verify(finding, values[provider])
    report.scope["checked"].append(f"Live verification: {len(values)} provider types")


def render_json(report: Report) -> str:
    return report.to_json()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--history", action="store_true", help="also scan added lines in git history")
    ap.add_argument("--verify", action="store_true", help="send each key to the provider (network)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", default="")
    ap.add_argument("--max-files", type=int, default=MAX_FILES)
    ap.add_argument("--suppress", default="", help="JSON Lines ignore file")
    args = ap.parse_args()
    if not os.path.exists(args.target):
        sys.exit(f"not found: {args.target}")
    report = build_report(args.target, args.history, args.verify, args.max_files)
    if args.suppress:
        suppress.apply_file(report, args.suppress)
    text = report.to_json() if args.json else render_text(report)
    print(text)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out + ".json", "w", encoding="utf-8") as fh:
            fh.write(report.to_json() + "\n")
        with open(args.out + ".md", "w", encoding="utf-8") as fh:
            fh.write(render_text(report) + "\n")


def render_text(report: Report) -> str:
    lines = [f"# Secret scan: {report.target}", "", f"Masked values. {len(report.findings)} matches.", ""]
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    for f in sorted(report.findings, key=lambda x: order.get(x.severity, 9)):
        lines.append(f"- [{f.severity}/{f.confidence}] {f.title}: {f.evidence}")
        lines.append(f"  - {f.fix}")
    lines += ["", "Values are masked. Revoke first, clean history second.", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    main()
