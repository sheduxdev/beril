#!/usr/bin/env python3
"""AST rules for Python and JavaScript.

Regex rules see a line. These rules see a call shape and its keywords, which
removes the worst noise (a string that mentions ``eval`` is not an eval call).
Python uses ``ast`` from the stdlib. JavaScript uses ``esprima`` when installed;
a parse failure returns no findings and leaves the regex rules in charge.

    python scripts/ast_rules.py --target ./src
"""

from __future__ import annotations

import argparse
import ast
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from beril_model import Finding

MAX_FINDINGS = 20


def _finding(
    rel: str,
    line: int,
    rule: str,
    title: str,
    severity: str,
    impact: str,
    fix: str,
    cwe: str,
    confidence: str = "medium",
) -> Finding:
    return Finding(
        check="ast." + rule,
        title=title,
        severity=severity,
        confidence=confidence,
        evidence=f"{rel}:{line}",
        impact=impact,
        fix=fix,
        subject=f"{rel}:{line}",
        source="static",
        cwe=[cwe],
        tags=["ast"],
        false_positive="An AST match still needs the data flow checked.",
    )


class _PythonVisitor(ast.NodeVisitor):
    def __init__(self, rel: str) -> None:
        self.rel = rel
        self.out: list[Finding] = []

    def add(
        self,
        node: ast.AST,
        rule: str,
        title: str,
        severity: str,
        impact: str,
        fix: str,
        cwe: str,
        confidence: str = "medium",
    ) -> None:
        if len(self.out) < MAX_FINDINGS:
            self.out.append(
                _finding(self.rel, getattr(node, "lineno", 1), rule, title, severity, impact, fix, cwe, confidence)
            )

    def visit_Call(self, node: ast.Call) -> None:
        name = _dotted(node.func)
        if name in ("eval", "exec"):
            self.add(
                node,
                "eval",
                "Dynamic code evaluation",
                "medium",
                "A crafted string runs as code.",
                "Prefer a literal or a restricted evaluator.",
                "CWE-95",
            )
        if name in ("os.system", "os.popen"):
            self.add(
                node,
                "system",
                "Shell execution",
                "medium",
                "Input through the shell can inject a command.",
                "Pass a list to subprocess, or quote the argument.",
                "CWE-78",
            )
        if name.startswith("subprocess.") and _keyword(node, "shell") is True:
            self.add(
                node,
                "shell-true",
                "subprocess with shell=True",
                "medium",
                "A shell parses the command line.",
                "Pass a list and drop shell=True.",
                "CWE-78",
            )
        if name.endswith((".execute", ".executemany")) and node.args and _dynamic(node.args[0]):
            self.add(
                node,
                "sql-expression",
                "SQL built from an expression",
                "high",
                "A quote in the value changes the query.",
                "Pass parameters as the second argument.",
                "CWE-89",
                "high",
            )
        if name == "yaml.load" and _keyword(node, "Loader") is None:
            self.add(
                node,
                "yaml-load",
                "yaml.load without a Loader",
                "medium",
                "The default loader can build arbitrary objects.",
                "Use yaml.safe_load or Loader=SafeLoader.",
                "CWE-502",
            )
        if name.startswith("pickle.") or name in ("pickle.load", "pickle.loads"):
            self.add(
                node,
                "pickle",
                "pickle deserialization",
                "medium",
                "A crafted stream can run code.",
                "Only load trusted data, or sign it.",
                "CWE-502",
                "low",
            )
        if name.startswith("requests.") and _keyword(node, "timeout") is None:
            self.add(
                node,
                "requests-timeout",
                "requests call without a timeout",
                "low",
                "A hung peer holds the worker.",
                "Pass timeout=(3, 10).",
                "CWE-400",
            )
        if name.startswith("jwt.") and _keyword(node, "algorithms") is None:
            self.add(
                node,
                "jwt-algorithms",
                "jwt call without an algorithm list",
                "medium",
                "The token header picks the algorithm.",
                "Pass algorithms=[...].",
                "CWE-347",
            )
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if node.attr == "md5":
            self.add(
                node,
                "md5",
                "MD5 used",
                "low",
                "Collisions are cheap.",
                "Use SHA-256 unless the format requires MD5.",
                "CWE-328",
            )
        self.generic_visit(node)


def _dotted(node: ast.AST) -> str:
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
    return ".".join(reversed(parts))


def _keyword(node: ast.Call, name: str) -> object:
    for keyword in node.keywords:
        if keyword.arg == name:
            if isinstance(keyword.value, ast.Constant):
                return keyword.value.value
            return keyword.value
    return None


def _dynamic(node: ast.AST) -> bool:
    return isinstance(node, ast.JoinedStr | ast.BinOp) or (
        isinstance(node, ast.Call) and _dotted(node.func) == "format"
    )


def scan_python(rel: str, text: str) -> list[Finding]:
    """Parse Python and return AST findings.

    Args:
        rel: Path shown in evidence.
        text: Source.

    Returns:
        Findings, empty on a syntax error.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    visitor = _PythonVisitor(rel)
    visitor.visit(tree)
    return visitor.out


def _js_line(node: dict) -> int:
    return int((node.get("loc") or {}).get("start", {}).get("line", 1))


def _js_walk(node: object, rel: str, out: list[Finding]) -> None:
    if isinstance(node, list):
        for item in node:
            _js_walk(item, rel, out)
        return
    if not isinstance(node, dict):
        return
    if node.get("type") == "CallExpression" and len(out) < MAX_FINDINGS:
        callee = node.get("callee") or {}
        args = node.get("args") or node.get("arguments") or []
        name = callee.get("name", "")
        prop = (callee.get("property") or {}).get("name", "")
        obj_node = callee.get("object") or {}
        obj = obj_node.get("name", "")
        if not obj and obj_node.get("type") == "CallExpression":
            required = (obj_node.get("arguments") or [{}])[0]
            obj = required.get("value", "") if isinstance(required, dict) else ""
        line = _js_line(node)
        if name == "eval" or (name == "Function" and args):
            out.append(
                _finding(
                    rel,
                    line,
                    "eval",
                    "Dynamic code evaluation",
                    "medium",
                    "A crafted string runs as code.",
                    "Prefer a literal or a parser.",
                    "CWE-95",
                )
            )
        if obj in ("child_process", "cp") and prop in ("exec", "execSync"):
            out.append(
                _finding(
                    rel,
                    line,
                    "child-process",
                    "Shell execution",
                    "medium",
                    "Input through the shell can inject a command.",
                    "Use execFile, or quote the argument.",
                    "CWE-78",
                )
            )
        if obj == "crypto" and prop == "createHash" and args and args[0].get("value") == "md5":
            out.append(
                _finding(rel, line, "md5", "MD5 used", "low", "Collisions are cheap.", "Use sha256.", "CWE-328", "high")
            )
        if prop in ("send", "write") and args and _js_from_request(args[0]):
            out.append(
                _finding(
                    rel,
                    line,
                    "xss-response",
                    "Request value written to the response",
                    "medium",
                    "Script in the value runs in the browser.",
                    "Encode or use a template.",
                    "CWE-79",
                )
            )
        if prop in ("redirect", "assign") and args and _js_from_request(args[0]):
            out.append(
                _finding(
                    rel,
                    line,
                    "open-redirect",
                    "Redirect from request input",
                    "medium",
                    "The link can leave the site.",
                    "Allowlist relative paths.",
                    "CWE-601",
                )
            )
    for value in node.values():
        if isinstance(value, dict | list):
            _js_walk(value, rel, out)


def _js_from_request(node: dict) -> bool:
    text: object = node
    for _ in range(20):
        if not isinstance(text, dict) or not text:
            return False
        if text.get("name") in ("req", "request", "ctx"):
            return True
        text = text.get("object") or text.get("callee") or {}
    return False


def scan_js(rel: str, text: str) -> list[Finding]:
    """Parse JavaScript with esprima and return AST findings.

    Args:
        rel: Path shown in evidence.
        text: Source.

    Returns:
        Findings, empty when esprima is absent or parsing fails.
    """
    try:
        import esprima
    except ImportError:
        return []
    try:
        tree = esprima.parseScript(text, {"loc": True})
    except Exception:
        return []
    out: list[Finding] = []
    _js_walk(tree.toDict(), rel, out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    args = ap.parse_args()
    root = Path(args.target)
    files = [root] if root.is_file() else [p for p in root.rglob("*") if p.suffix in (".py", ".js", ".ts")]
    total = 0
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = str(path)
        findings = scan_python(rel, text) if path.suffix == ".py" else scan_js(rel, text)
        for finding in findings:
            print(f"{finding.severity:8} {finding.check:24} {finding.evidence}")
        total += len(findings)
    print(f"\n{total} findings", file=sys.stderr)


if __name__ == "__main__":
    main()
