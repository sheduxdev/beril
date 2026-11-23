#!/usr/bin/env python3
"""MCP configuration linter and secret pass.

Walks a project for MCP client configs, parses them and reports: unpinned
packages, plaintext keys, broad filesystem access, remote transports without
TLS, dangerous container flags and tool descriptions that look like injected
instructions.

Never launches an MCP server.

    python scripts/scan_mcp.py --target .
    python scripts/scan_mcp.py --target ~/.config/Claude --json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import beril_secrets as secret_mod
import fileio
import paths
import suppress
from beril_model import Finding, Report

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NAMES = {
    "mcp.json",
    "claude_desktop_config.json",
    ".mcp.json",
    "mcp-config.json",
    "mcp_servers.json",
    "cursor-mcp.json",
}
SKIP = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".next"}
SUPPLY_NAMES = {
    "plugin.json",
    "gemini-extension.json",
    "marketplace.json",
    "SKILL.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "OPENAI.md",
}
SUPPLY_EXT = {".mdc"}
MAX_SUPPLY = 300
MAX_CONFIGS = 200
UNPINNED = re.compile(r"\b(npx|bunx|uvx|pnpm\s+dlx)\b")
PIN = re.compile(r"@\d+(?:\.\d+){0,2}\b|@latest\b|@next\b|@canary\b")


def load_rules() -> dict:
    try:
        with open(os.path.join(paths.DATA, "mcp_rules.json"), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError):
        return {"instruction_patterns": [], "risky_args": [], "supply_chain": []}


def find_configs(root: str) -> list[Path]:
    rootp = Path(root)
    if rootp.is_file():
        return [rootp] if rootp.suffix == ".json" else []
    found = []
    for dirpath, dirnames, filenames in os.walk(rootp):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in filenames:
            path = Path(dirpath) / name
            if name in NAMES or (name.endswith(".json") and "mcp" in name.lower()):
                found.append(path)
            if len(found) >= MAX_CONFIGS:
                return found
    return found


def find_supply_files(root: str) -> list[Path]:
    rootp = Path(root)
    if rootp.is_file():
        return [rootp] if rootp.name in SUPPLY_NAMES or rootp.suffix in SUPPLY_EXT else []
    found = []
    for dirpath, dirnames, filenames in os.walk(rootp):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        for name in filenames:
            if name in SUPPLY_NAMES or Path(name).suffix in SUPPLY_EXT:
                found.append(Path(dirpath) / name)
                if len(found) >= MAX_SUPPLY:
                    return found
    return found


def scan_supply_chain(root: str, rules: dict) -> list[Finding]:
    out = []
    for path in find_supply_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")[:200_000]
        except OSError:
            continue
        for rule in rules.get("supply_chain", []):
            for match in re.finditer(rule["regex"], text, re.M):
                line = text[: match.start()].count("\n") + 1
                out.append(
                    Finding(
                        check="mcp.supply." + re.sub(r"\W+", "-", rule["title"]).lower()[:40],
                        title=rule["title"],
                        severity=rule["severity"],
                        confidence="medium",
                        evidence=f"{path}:{line} {match.group(0).strip()[:120]}",
                        impact="Supply-chain review lead for a skill, agent or plugin manifest.",
                        fix=rule["fix"],
                        subject=f"{path}:{line}",
                        source="static",
                        cwe=["CWE-1104"],
                        tags=["supply-chain"],
                        false_positive=rule.get("false_positive", ""),
                    )
                )
        if path.name in ("plugin.json", "gemini-extension.json"):
            try:
                data = json.loads(text)
            except json.JSONDecodeError:
                continue
            for key, severity, fix in (
                ("version", "medium", "Set a version so a host can pin the plugin."),
                ("license", "low", "State the licence."),
                ("repository", "low", "Point at the source repository."),
            ):
                if not data.get(key):
                    out.append(
                        Finding(
                            check=f"mcp.supply.manifest-{key}",
                            title=f"Plugin manifest has no {key}",
                            severity=severity,
                            confidence="high",
                            evidence=str(path),
                            impact="The host cannot pin or trace the plugin.",
                            fix=fix,
                            subject=str(path),
                            source="static",
                            cwe=["CWE-1104"],
                            tags=["supply-chain"],
                        )
                    )
    return out


def parse(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    text = re.sub(r"^\s*//.*$", "", text, flags=re.M)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def servers_of(data: dict) -> dict:
    if isinstance(data.get("mcpServers"), dict):
        return data["mcpServers"]
    if isinstance(data.get("servers"), dict):
        return data["servers"]
    if isinstance(data.get("mcp"), dict) and isinstance(data["mcp"].get("servers"), dict):
        return data["mcp"]["servers"]
    return {}


def scan_server(path: str, server: str, cfg: dict, rules: dict) -> list[Finding]:
    out: list[Finding] = []
    command = cfg.get("command", "") if isinstance(cfg.get("command", ""), str) else ""
    args = cfg.get("args", []) or []
    arg_text = " ".join(str(a) for a in args) if isinstance(args, list) else str(args)
    url = cfg.get("url", "") if isinstance(cfg.get("url", ""), str) else ""
    env = cfg.get("env", {}) if isinstance(cfg.get("env", {}), dict) else {}
    subject = f"{path}#{server}"

    if (UNPINNED.search(command) or UNPINNED.search(arg_text)) and not PIN.search(arg_text):
        out.append(
            Finding(
                check="mcp.unpinned",
                title=f"Unpinned package: {server}",
                severity="medium",
                confidence="high",
                evidence=f"{subject}: {command} {arg_text[:160]}",
                impact="Every launch pulls a new version, so a supply chain attack lands directly.",
                fix="Pin the package version (example@1.2.3) and verify a hash when possible.",
                subject=subject,
                cwe=["CWE-1104"],
                tags=["supply-chain"],
                source="static",
                false_positive="latest can be deliberate during development.",
            )
        )
    for rule in rules.get("risky_args", []):
        if re.search(rule["match"], arg_text):
            out.append(
                Finding(
                    check="mcp.arg." + re.sub(r"\W+", "-", rule["title"]).strip("-").lower(),
                    title=f"{rule['title']}: {server}",
                    severity=rule["severity"],
                    confidence="medium",
                    evidence=f"{subject}: {arg_text[:200]}",
                    impact="The agent reach is wide.",
                    fix=rule["fix"],
                    subject=subject,
                    source="static",
                    tags=["permission"],
                )
            )
    if re.search(r"(?:^|\s)(?:/|~|\$HOME)(?:\s|$)", arg_text) and not re.search(r"/[\w.-]+/", arg_text):
        out.append(
            Finding(
                check="mcp.broad-fs",
                title=f"Broad filesystem access: {server}",
                severity="medium",
                confidence="medium",
                evidence=f"{subject}: {arg_text[:160]}",
                impact="The agent can read the root or home directory, including secrets and SSH keys.",
                fix="Pass the project directory only.",
                subject=subject,
                cwe=["CWE-732"],
            )
        )
    if url:
        if url.startswith("http://"):
            out.append(
                Finding(
                    check="mcp.remote-plain",
                    title=f"Remote MCP over plain HTTP: {server}",
                    severity="medium",
                    confidence="high",
                    evidence=f"{subject}: {url[:160]}",
                    impact="Tool definitions and responses can change in transit.",
                    fix="Use HTTPS or a tunnel.",
                    subject=subject,
                    cwe=["CWE-319"],
                )
            )
        if "@" in url and "://" in url:
            out.append(
                Finding(
                    check="mcp.url-userinfo",
                    title=f"Credentials in the URL: {server}",
                    severity="low",
                    confidence="high",
                    evidence=f"{subject}: {re.sub(r'//[^@]+@', '//***@', url)[:160]}",
                    impact="The token sits in the file in clear text.",
                    fix="Move the token to an environment variable.",
                    subject=subject,
                    cwe=["CWE-798"],
                )
            )
        if not cfg.get("headers"):
            out.append(
                Finding(
                    check="mcp.remote-no-header",
                    title=f"No auth header on a remote server: {server}",
                    severity="low",
                    confidence="low",
                    evidence=subject,
                    impact="The endpoint may be public with no authorization boundary.",
                    fix="Add an Authorization header when needed and narrow the scope.",
                    subject=subject,
                    false_positive="Some servers need no authentication.",
                )
            )
    for key, value in env.items():
        if not isinstance(value, str):
            continue
        if (
            re.search(r"(?i)(key|token|secret|pass|credential)", str(key))
            and not value.startswith("${")
            and len(value) >= 8
        ):
            out.append(
                Finding(
                    check="mcp.plain-secret",
                    title=f"Plain key in env: {key}",
                    severity="high",
                    confidence="medium",
                    evidence=f"{subject}: {key}={secret_mod.mask(value)}",
                    impact="Sharing the config leaks the key.",
                    fix="Move the value to the shell environment or a secret store and use ${VAR}.",
                    subject=subject,
                    cwe=["CWE-798"],
                    tags=["secret"],
                )
            )
    description = cfg.get("description", "") + " " + str(cfg.get("instructions", ""))
    for pattern in rules.get("instruction_patterns", []):
        if re.search(pattern, description):
            out.append(
                Finding(
                    check="mcp.description-instruction",
                    title=f"Tool description contains instructions: {server}",
                    severity="low",
                    confidence="medium",
                    evidence=f"{subject}: {re.search(pattern, description).group(0)[:120]}",
                    impact="A typical surface for tool poisoning.",
                    fix="Compare the description with its source and note unexpected instructions.",
                    subject=subject,
                    cwe=["CWE-1426"],
                    tags=["prompt-injection"],
                    false_positive="Well written descriptions use commands too.",
                )
            )
    return out


def scan(target: str) -> Report:
    report = Report(target=target, mode="mcp")
    report.scope["checked"] = [
        "MCP client configs",
        "Version pinning",
        "Plain keys",
        "Filesystem and container permissions",
        "Remote transport TLS",
        "Description instructions",
    ]
    report.scope["not_checked"] = [
        "Server runtime behavior",
        "Tool output poisoning test",
        "OAuth flows",
        "Corporate policy fit",
    ]
    rules = load_rules()
    supply = scan_supply_chain(target, rules)
    for finding in supply:
        report.add(finding)
    if supply:
        report.scope["checked"].append("Skill, agent and plugin manifests")
    configs = find_configs(target)
    if not configs:
        report.errors.append("No MCP config found" if not supply else "No MCP config found, only supply files")
        report.finish()
        return report
    for path in configs:
        data = parse(path)
        if data is None:
            report.add(
                Finding(
                    check="mcp.parse",
                    title="Config cannot be parsed",
                    severity="low",
                    confidence="high",
                    evidence=str(path),
                    impact="Rules could not run.",
                    fix="Fix the JSON syntax.",
                    subject=str(path),
                )
            )
            continue
        servers = servers_of(data)
        if not servers:
            continue
        report.add(
            Finding(
                check="mcp.config",
                title=f"MCP config: {len(servers)} servers",
                severity="info",
                confidence="high",
                evidence=str(path),
                impact="Surface to review.",
                fix="Verify each server for source and permissions.",
                subject=str(path),
            )
        )
        for name, cfg in servers.items():
            if isinstance(cfg, dict):
                for finding in scan_server(str(path), str(name), cfg, rules):
                    report.add(finding)
    report.finish()
    return report


def render(report: Report) -> str:
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    lines = [f"# MCP audit: {report.target}", "", f"{len(report.findings)} findings.", ""]
    for f in sorted(report.findings, key=lambda x: order.get(x.severity, 9)):
        lines.append(f"- [{f.severity}/{f.confidence}] {f.title}: {f.evidence}")
        lines.append(f"  - {f.fix}")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--suppress", default="", help="JSON Lines ignore file")
    args = ap.parse_args()
    if not os.path.exists(args.target):
        sys.exit(f"not found: {args.target}")
    report = scan(args.target)
    if args.suppress:
        suppress.apply_file(report, args.suppress)
    print(report.to_json() if args.json else render(report))
    if args.out:
        fileio.write_json(args.out + ".json", report.to_dict())
        fileio.write_text(args.out + ".md", render(report) + "\n")


if __name__ == "__main__":
    main()
