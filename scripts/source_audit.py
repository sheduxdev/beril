#!/usr/bin/env python3
"""Source rule engine used by scan_artifact and hunt.

Loads data/source_rules.json, applies language filters and turns line hits into
findings. Also computes two structural signals: dependency fan-in (a helper
imported by many modules is a single failure point) and silent except density.

Rules are known static classes, not novel research. The value is the report
discipline around them: every hit names a line, a CWE, a fix and a false
positive note.
"""

from __future__ import annotations

import collections
import json
import os
import re

import ast_rules
import paths
from beril_model import Finding

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LANG_BY_EXT = {
    ".py": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".php": "php",
    ".java": "java",
    ".kt": "java",
    ".go": "go",
    ".rb": "ruby",
    ".rs": "rust",
    ".c": "c",
    ".h": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".sh": "shell",
    ".ps1": "powershell",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".tf": "terraform",
    ".dockerfile": "docker",
    ".sql": "sql",
}
DOCKER_NAMES = {"Dockerfile", "docker-compose.yml", "docker-compose.yaml", "compose.yml"}
MAX_HITS = 4

IMPORT_RE = {
    "python": re.compile(r"^\s*(?:from\s+([\w.]+)\s+import|import\s+([\w.]+))", re.M),
    "javascript": re.compile(r"""(?:from\s+['"]([^'"]+)['"]|require\(\s*['"]([^'"]+)['"]\s*\))"""),
    "typescript": re.compile(r"""(?:from\s+['"]([^'"]+)['"]|require\(\s*['"]([^'"]+)['"]\s*\))"""),
    "go": re.compile(r'^\s*"([\w./-]+)"\s*$', re.M),
}


_RULES: list[dict] | None = None


def load_rules() -> list[dict]:
    global _RULES
    if _RULES is not None:
        return _RULES
    try:
        with open(os.path.join(paths.DATA, "source_rules.json"), encoding="utf-8") as fh:
            _RULES = json.load(fh).get("rules", [])
    except (OSError, json.JSONDecodeError):
        _RULES = []
    try:
        with open(os.path.join(paths.DATA, "incidents.jsonl"), encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    rule = json.loads(line).get("rule")
                    if rule:
                        _RULES.append(rule)
    except (OSError, json.JSONDecodeError):
        pass
    return _RULES or []


def lang_of(path: str, name: str) -> str:
    if name in DOCKER_NAMES:
        return "docker"
    return LANG_BY_EXT.get(os.path.splitext(name)[1].lower(), "")


def scan_text(rel: str, text: str, lang: str) -> list[Finding]:
    out: list[Finding] = []
    seen = collections.Counter()
    for rule in load_rules():
        if rule.get("regex") is None:
            continue
        allowed = rule.get("languages")
        if allowed and lang not in allowed:
            continue
        if seen[rule["id"]] >= MAX_HITS:
            continue
        pattern = re.compile(rule["regex"], re.M)
        for match in pattern.finditer(text):
            line = text[: match.start()].count("\n") + 1
            seen[rule["id"]] += 1
            out.append(
                Finding(
                    check="src." + rule["id"],
                    title=rule["title"],
                    severity=rule["severity"],
                    confidence=rule["confidence"],
                    evidence=f"{rel}:{line} {match.group(0)[:120].strip()}",
                    impact=rule["impact"],
                    fix=rule["fix"],
                    subject=f"{rel}:{line}",
                    source="static",
                    cwe=rule.get("cwe", []),
                    tags=["source-rule"],
                    false_positive=rule.get("false_positive", ""),
                )
            )
            if seen[rule["id"]] >= MAX_HITS:
                break
    if lang == "python":
        bare = len(re.findall(r"^\s*except\s*:", text, re.M))
        if bare >= 5:
            out.append(
                Finding(
                    check="src.bare-except-density",
                    title=f"Bare except density ({bare})",
                    severity="low",
                    confidence="medium",
                    evidence=f"{rel}: {bare} adet",
                    impact="Errors are swallowed and an empty result can look like success.",
                    fix="Catch narrow exception types and log them.",
                    subject=rel,
                    source="static",
                    cwe=["CWE-703"],
                    tags=["source-rule"],
                )
            )
        globals_count = len(re.findall(r"^\s*global\s+\w+", text, re.M))
        if globals_count >= 10:
            out.append(
                Finding(
                    check="src.global-state",
                    title=f"Heavy global state ({globals_count})",
                    severity="low",
                    confidence="medium",
                    evidence=f"{rel}: {globals_count} global",
                    impact="Race conditions in concurrent use and harder tests.",
                    fix="Move state into a class or a context object.",
                    subject=rel,
                    source="static",
                    cwe=["CWE-362"],
                    tags=["source-rule"],
                )
            )
    if lang == "python":
        out.extend(ast_rules.scan_python(rel, text))
    elif lang in ("javascript", "typescript"):
        out.extend(ast_rules.scan_js(rel, text))
    return out


def fan_in(files: dict[str, str]) -> list[Finding]:
    """files: rel path -> text. A local module imported by many files is a risk."""
    counts = collections.Counter()
    for path, text in files.items():
        lang = LANG_BY_EXT.get(os.path.splitext(path)[1].lower(), "")
        pattern = IMPORT_RE.get(lang)
        if not pattern:
            continue
        for match in pattern.finditer(text):
            module = match.group(1) or (match.group(2) if match.lastindex and match.lastindex > 1 else "")
            if not module or module.startswith((".", "/")):
                continue
            module = module.split(".")[0].split("/")[0]
            counts[module] += 1
    out = []
    total = max(len(files), 1)
    for module, count in counts.most_common(3):
        if count < max(5, total // 8):
            continue
        out.append(
            Finding(
                check="src.fan-in",
                title=f"Single point of failure: {module}",
                severity="low",
                confidence="medium",
                evidence=f"{module}: imported in {count} files ({total} total)",
                impact=f"If the shared component breaks, {count} modules fall with it.",
                fix="Add tests, a contract and a fallback to the critical helper.",
                subject=module,
                source="static",
                cwe=["CWE-1061"],
                tags=["architecture"],
            )
        )
    return out
