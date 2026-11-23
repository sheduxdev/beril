#!/usr/bin/env python3
"""Adapters that run specialist tools and return Beril findings.

Beril does not reimplement Nuclei, Semgrep, Trivy or TruffleHog. It runs the
installed binary with a safe argument list, parses JSON or SARIF and maps each
result into the shared schema. Missing tools are named, not simulated.

Each adapter is read-only or local by default. Nuclei and testssl send traffic,
so the caller must hold an ownership record.

    from adapters import AVAILABLE, run
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from dataclasses import dataclass

from beril_model import Finding, validate_finding_dict

MAX_OUTPUT = 8_000_000
ZAP_REPORT = "zap-report.json"
DEFAULT_TIMEOUT = 420

SEVERITY_MAP = {
    "critical": "critical",
    "high": "high",
    "error": "high",
    "medium": "medium",
    "warning": "medium",
    "low": "low",
    "note": "low",
    "info": "info",
    "informational": "info",
    "unknown": "info",
}


@dataclass
class Tool:
    name: str
    binary: str
    kind: str
    active: bool
    description: str


TOOLS = {
    "nuclei": Tool("nuclei", "nuclei", "web", True, "Template scanner for known CVEs and exposures"),
    "semgrep": Tool("semgrep", "semgrep", "source", False, "SAST rules over a source tree"),
    "trivy": Tool("trivy", "trivy", "artifact", False, "Dependency, secret, config and image scan"),
    "gitleaks": Tool("gitleaks", "gitleaks", "source", False, "Secret scan with git history"),
    "osv-scanner": Tool("osv-scanner", "osv-scanner", "source", False, "Dependency match against OSV"),
    "syft": Tool("syft", "syft", "artifact", False, "SBOM generation"),
    "grype": Tool("grype", "grype", "artifact", False, "Vulnerability scan from an SBOM or image"),
    "testssl": Tool("testssl", "testssl.sh", "web", True, "TLS configuration and certificate test"),
    "zap": Tool("zap", "zap-baseline.py", "web", True, "ZAP baseline scan, parsed from a JSON report"),
}
AVAILABLE = {name: bool(shutil.which(tool.binary)) for name, tool in TOOLS.items()}


def run_tool(
    name: str,
    target: str,
    workdir: str = "",
    headers: dict | None = None,
    timeout: int = DEFAULT_TIMEOUT,
    offline: bool = False,
) -> tuple[str, str, int]:
    """Run one adapter command.

    Args:
        name: Adapter key.
        target: URL, file or directory.
        workdir: Working directory for tools that need one.
        headers: Extra HTTP headers for active tools.
        timeout: Seconds before the tool is killed.
        offline: Pass offline flags where the tool supports them.

    Returns:
        stdout, stderr and exit code.
    """
    tool = TOOLS[name]
    if not AVAILABLE[name]:
        return "", f"{tool.binary} not installed", 127
    args = build_args(name, target, headers or {}, offline)
    try:
        proc = subprocess.run(
            args, capture_output=True, text=True, timeout=timeout, cwd=workdir or None, errors="replace"
        )
        return (proc.stdout or "")[:MAX_OUTPUT], (proc.stderr or "")[:20_000], proc.returncode
    except subprocess.TimeoutExpired:
        return "", f"timeout after {timeout}s", 124
    except Exception as exc:
        return "", f"{type(exc).__name__}: {exc}", 1


def build_args(name: str, target: str, headers: dict, offline: bool) -> list[str]:
    if name == "nuclei":
        args = [TOOLS[name].binary, "-u", target, "-jsonl", "-silent", "-severity", "low,medium,high,critical"]
        for key, value in headers.items():
            args += ["-H", f"{key}: {value}"]
        return args
    if name == "semgrep":
        return [TOOLS[name].binary, "--config", "auto", "--json", "--quiet", target]
    if name == "trivy":
        args = [TOOLS[name].binary, "fs", "--format", "json", "--scanners", "vuln,secret,misconfig", target]
        if offline:
            args += ["--offline-scan"]
        return args
    if name == "gitleaks":
        return [TOOLS[name].binary, "dir", target, "--report-format", "json", "--report-path", "-", "--no-banner"]
    if name == "osv-scanner":
        return [TOOLS[name].binary, "scan", "source", "-r", "--format", "json", target]
    if name == "syft":
        return [TOOLS[name].binary, target, "-o", "cyclonedx-json", "-q"]
    if name == "grype":
        return [TOOLS[name].binary, target, "-o", "json", "-q"]
    if name == "testssl":
        return [TOOLS[name].binary, "--jsonfile", "-", "--quiet", target]
    if name == "zap":
        return [TOOLS[name].binary, "-t", target, "-J", "zap-report.json", "-q"]
    return [TOOLS[name].binary, target]


def _cwe(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if item]
    if value:
        return [str(value)]
    return []


def _text(value: object, limit: int = 400) -> str:
    text = re.sub(r"<[^>]+>", " ", str(value or ""))
    return re.sub(r"\s+", " ", text).strip()[:limit]


def _finding(
    check: str,
    title: str,
    severity: str,
    evidence: str,
    impact: str,
    fix: str,
    subject: str,
    confidence: str = "medium",
    **kwargs: object,
) -> Finding:
    title = (title or check)[:180]
    evidence = (evidence or subject or check)[:600]
    return Finding(
        check=check,
        title=title,
        severity=SEVERITY_MAP.get(str(severity).lower(), "info"),
        confidence=confidence,
        evidence=evidence,
        impact=(impact or "Imported finding. Replay before reporting.")[:500],
        fix=(fix or "Read the source rule and fix at the source.")[:600],
        subject=(subject or evidence)[:300],
        source="tool",
        cwe=kwargs.get("cwe", []),
        tags=kwargs.get("tags", []),
        false_positive=kwargs.get("false_positive", ""),
        refs=kwargs.get("refs", []),
    )


def parse_nuclei(stdout: str) -> list[Finding]:
    out = []
    for line in stdout.splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        info = item.get("info", {})
        name = item.get("template-id", "nuclei")
        matched = item.get("matched-at") or item.get("host", "")
        out.append(
            _finding(
                check="tool.nuclei." + re.sub(r"\W+", "-", name.lower())[:60],
                title=f"nuclei: {info.get('name', name)}",
                severity=info.get("severity", "info"),
                evidence=f"{matched} [{name}]",
                impact=(info.get("description") or "Template match. Replay before reporting.")[:400],
                fix="Read the template and the reference, then confirm the fix path.",
                subject=matched,
                confidence="medium",
                tags=["nuclei"],
                refs=[info["reference"]] if isinstance(info.get("reference"), str) else [],
                false_positive="Template can match a version banner without exploitability.",
            )
        )
    return out


def parse_semgrep(stdout: str) -> list[Finding]:
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return []
    out = []
    for item in data.get("results", []):
        path = item.get("path", "")
        line = item.get("start", {}).get("line", 0)
        extra = item.get("extra", {})
        out.append(
            _finding(
                check="tool.semgrep." + re.sub(r"\W+", "-", item.get("check_id", "rule"))[-60:],
                title="semgrep: " + (item.get("check_id", "rule").split(".")[-1]),
                severity=extra.get("severity", "medium"),
                evidence=f"{path}:{line} {(extra.get('lines') or '').strip()[:160]}",
                impact=(extra.get("message") or "Static rule match.")[:400],
                fix="Follow the data flow and fix at the source, not the sink.",
                subject=f"{path}:{line}",
                confidence="low",
                cwe=_cwe(extra.get("metadata", {}).get("cwe")),
                tags=["semgrep"],
                false_positive="SAST rule can fire on safe code. Confirm reachability.",
            )
        )
    return out


def parse_trivy(stdout: str) -> list[Finding]:
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return []
    out = []
    for result in data.get("Results", []):
        target = result.get("Target", "")
        for vuln in result.get("Vulnerabilities", []) or []:
            fixed = vuln.get("FixedVersion", "")
            out.append(
                _finding(
                    check="tool.trivy." + (vuln.get("VulnerabilityID") or "cve").lower(),
                    title=f"trivy: {vuln.get('VulnerabilityID')} in {vuln.get('PkgName')}",
                    severity=vuln.get("Severity", "medium"),
                    evidence=f"{target}: {vuln.get('PkgName')} {vuln.get('InstalledVersion')}",
                    impact=(vuln.get("Title") or "Known package vulnerability.")[:400],
                    fix=(f"Upgrade to {fixed}. " if fixed else "Find the fixed version. ")
                    + "Check whether the package is imported.",
                    subject=f"{target}:{vuln.get('PkgName')}",
                    confidence="medium",
                    tags=["trivy", "dependency"],
                )
            )
        for secret in result.get("Secrets", []) or []:
            out.append(
                _finding(
                    check="tool.trivy.secret",
                    title=f"trivy secret: {secret.get('Title', 'secret')}",
                    severity=secret.get("Severity", "high"),
                    evidence=f"{target}:{secret.get('StartLine', 0)} {secret.get('Match', '')[:120]}",
                    impact="A secret sits in the tree or image.",
                    fix="Revoke first, then remove and rotate.",
                    subject=f"{target}:{secret.get('StartLine', 0)}",
                    confidence="medium",
                    tags=["secret"],
                )
            )
        for misconfig in result.get("Misconfigurations", []) or []:
            out.append(
                _finding(
                    check="tool.trivy.config." + re.sub(r"\W+", "-", misconfig.get("ID", "rule")).lower(),
                    title=f"trivy config: {misconfig.get('Title', misconfig.get('ID'))}",
                    severity=misconfig.get("Severity", "medium"),
                    evidence=f"{target}: {misconfig.get('Message', '')[:160]}",
                    impact=(misconfig.get("Description") or "Configuration gap.")[:400],
                    fix=(misconfig.get("Resolution") or "Apply the hardened setting.")[:500],
                    subject=target,
                    confidence="medium",
                    tags=["iac"],
                )
            )
    return out


def parse_gitleaks(stdout: str) -> list[Finding]:
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return []
    out = []
    for item in data or []:
        out.append(
            _finding(
                check="tool.gitleaks." + (item.get("RuleID") or "secret"),
                title=f"gitleaks: {item.get('RuleID', 'secret')}",
                severity="high",
                evidence=f"{item.get('File')}:{item.get('StartLine')}",
                impact="A secret is committed.",
                fix="Revoke, rotate, then clean history if needed.",
                subject=f"{item.get('File')}:{item.get('StartLine')}",
                confidence="medium",
                tags=["secret"],
            )
        )
    return out


def parse_osv(stdout: str) -> list[Finding]:
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return []
    out = []
    for result in data.get("results", []):
        source = (result.get("source") or {}).get("path", "")
        for pkg in result.get("packages", []):
            name = (pkg.get("package") or {}).get("name", "")
            version = (pkg.get("package") or {}).get("version", "")
            for vuln in pkg.get("vulnerabilities", []):
                out.append(
                    _finding(
                        check="tool.osv." + (vuln.get("id") or "vuln").lower(),
                        title=f"osv: {vuln.get('id')} in {name}",
                        severity="high",
                        evidence=f"{source}: {name} {version}",
                        impact=(vuln.get("summary") or "Known dependency vulnerability.")[:400],
                        fix="Upgrade to a fixed version and confirm the import path.",
                        subject=f"{name}@{version}",
                        confidence="low",
                        tags=["osv", "dependency"],
                        false_positive="Check reachability before prioritizing.",
                    )
                )
    return out


def parse_grype(stdout: str) -> list[Finding]:
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return []
    out = []
    for match in data.get("matches", []):
        vuln = match.get("vulnerability", {})
        artifact = match.get("artifact", {})
        out.append(
            _finding(
                check="tool.grype." + (vuln.get("id") or "vuln").lower(),
                title=f"grype: {vuln.get('id')} in {artifact.get('name')}",
                severity=vuln.get("severity", "medium"),
                evidence=f"{artifact.get('name')} {artifact.get('version')}",
                impact=(vuln.get("description") or "Known package vulnerability.")[:400],
                fix="Upgrade the package or rebuild the image.",
                subject=f"{artifact.get('name')}@{artifact.get('version')}",
                confidence="medium",
                tags=["grype", "dependency"],
            )
        )
    return out


def parse_testssl(stdout: str) -> list[Finding]:
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return []
    out = []
    for item in data:
        sev = item.get("severity", "INFO")
        if sev.upper() in ("OK", "INFO"):
            continue
        out.append(
            _finding(
                check="tool.testssl." + re.sub(r"\W+", "-", item.get("id", "finding")).lower(),
                title=f"testssl: {item.get('id', 'finding')}",
                severity=sev,
                evidence=item.get("finding", "")[:300],
                impact="TLS configuration weakness.",
                fix="Adjust the TLS profile and re-test.",
                subject=item.get("ip", ""),
                confidence="medium",
                tags=["tls"],
            )
        )
    return out


ZAP_RISK = {"3": "high", "2": "medium", "1": "low", "0": "info"}
ZAP_CONFIDENCE = {"3": "high", "2": "medium", "1": "low", "0": "low"}


def parse_zap(stdout: str) -> list[Finding]:
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError:
        return []
    out = []
    for site in data.get("site", []):
        for alert in site.get("alerts", []):
            instances = alert.get("instances") or [{}]
            for instance in instances[:20]:
                uri = instance.get("uri") or site.get("@name", "")
                risk = str(alert.get("riskcode", alert.get("risk", "")))
                confidence = str(alert.get("confidence", ""))
                evidence = " ".join(
                    part
                    for part in (
                        instance.get("method", ""),
                        uri,
                        instance.get("param", ""),
                        _text(instance.get("evidence", ""), 160),
                    )
                    if part
                )
                cwe = alert.get("cweid")
                out.append(
                    _finding(
                        check="tool.zap." + re.sub(r"\W+", "-", str(alert.get("pluginid", "alert")))[:40],
                        title="ZAP: " + _text(alert.get("alert"), 120),
                        severity=ZAP_RISK.get(risk, alert.get("riskdesc", "info").split(" ")[0]),
                        evidence=evidence or uri,
                        impact=_text(alert.get("desc")),
                        fix=_text(alert.get("solution")),
                        subject=uri,
                        confidence=ZAP_CONFIDENCE.get(confidence, "medium"),
                        cwe=[f"CWE-{cwe}"] if cwe else [],
                        tags=["zap"],
                        false_positive="ZAP alerts include passive banners and duplicates. Replay the instance.",
                        refs=[alert["reference"]] if isinstance(alert.get("reference"), str) else [],
                    )
                )
    return out


PARSERS = {
    "nuclei": parse_nuclei,
    "semgrep": parse_semgrep,
    "trivy": parse_trivy,
    "gitleaks": parse_gitleaks,
    "osv-scanner": parse_osv,
    "grype": parse_grype,
    "testssl": parse_testssl,
    "zap": parse_zap,
}


def validate_findings(findings: list[Finding]) -> list[str]:
    """Check findings against the shared schema.

    Args:
        findings: Parsed findings.

    Returns:
        Problem strings, prefixed with the check id.
    """
    problems = []
    for finding in findings:
        for problem in validate_finding_dict(finding.to_dict()):
            problems.append(f"{finding.check}: {problem}")
    return problems


def run(
    name: str, target: str, headers: dict | None = None, offline: bool = False, timeout: int = DEFAULT_TIMEOUT
) -> tuple[list[Finding], str]:
    """Run one adapter and parse its output.

    Args:
        name: Adapter key.
        target: URL, file or directory.
        headers: Extra headers for active tools.
        offline: Prefer offline mode.
        timeout: Seconds.

    Returns:
        Findings and an error string.
    """
    if name not in TOOLS:
        return [], f"unknown tool: {name}"
    if not AVAILABLE[name]:
        return [], f"{TOOLS[name].binary} not installed"
    stdout, stderr, code = run_tool(name, target, headers=headers, timeout=timeout, offline=offline)
    if name == "zap" and not stdout.lstrip().startswith(("{", "[")):
        try:
            with open(ZAP_REPORT, encoding="utf-8", errors="replace") as handle:
                stdout = handle.read()
        except OSError:
            pass
    parser = PARSERS.get(name)
    findings = parser(stdout) if parser else []
    problems = validate_findings(findings)
    if problems:
        return findings, "schema: " + "; ".join(problems[:5])
    if code not in (0, 1) and not findings:
        return [], f"exit {code}: {stderr[:300]}"
    return findings, ""


def list_tools() -> list[dict]:
    return [
        {
            "name": name,
            "installed": AVAILABLE[name],
            "kind": tool.kind,
            "active": tool.active,
            "description": tool.description,
        }
        for name, tool in TOOLS.items()
    ]
