#!/usr/bin/env python3
"""Optional deep triage for a binary. Runs only tools that are installed.

python scripts/re_triage.py --target ./sample --out scans/sample-re
python scripts/re_triage.py --target ./sample --capa --floss --rizin --ghidra
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import report_render
import scan_artifact
from beril_model import Finding


def tool(name: str) -> str:
    local = os.path.join(os.path.dirname(sys.executable), name)
    if os.path.exists(local):
        return local
    return shutil.which(name) or ""


def have(name: str) -> bool:
    return bool(tool(name))


def run(cmd: list[str], timeout: int = 120) -> tuple[int, str, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, errors="replace")
        return p.returncode, p.stdout, p.stderr
    except Exception as exc:
        return 1, "", f"{type(exc).__name__}: {exc}"


def add(findings: list[Finding], sev: str, title: str, evidence: str, advice: str, check: str) -> None:
    findings.append(
        Finding(
            check=check,
            title=title,
            severity=sev,
            confidence="medium",
            evidence=evidence[:600],
            impact=advice,
            fix=advice,
            subject=evidence.split(":", 1)[0][:200],
            source="tool",
        )
    )


def capa(path: str, findings: list[dict], timeout: int) -> dict:
    if not have("capa"):
        return {"status": "missing"}
    rules = os.environ.get("CAPA_RULES", os.path.expanduser("~/.capa/rules"))
    cmd = [tool("capa"), "-j"]
    if os.path.isdir(rules):
        cmd += ["-r", rules]
    sigs = os.environ.get("CAPA_SIGS", os.path.expanduser("~/.capa/sigs"))
    if os.path.isdir(sigs):
        cmd += ["-s", sigs]
    cmd.append(path)
    _code, out, err = run(cmd, timeout=timeout)
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return {"status": "failed", "error": err[:300]}
    rules = data.get("rules", {})
    summary = []
    for key, rule in list(rules.items())[:60]:
        meta = rule.get("meta", {})
        ns = meta.get("namespace", "")
        name = meta.get("name", key)
        sev = "medium" if any(x in ns for x in ("c2", "persistence", "anti-analysis", "credential")) else "info"
        add(findings, sev, "capa: " + name, ns or key, "Review the capability and its addresses.", "capa-" + key[:40])
        summary.append({"rule": name, "namespace": ns})
    return {"status": "ok", "rules": len(rules), "summary": summary[:60]}


def floss(path: str, findings: list[dict], timeout: int) -> dict:
    if not have("floss"):
        return {"status": "missing"}
    _code, out, err = run([tool("floss"), "-j", path], timeout=timeout)
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return {"status": "failed", "error": err[:300]}
    decoded = data.get("strings", {}).get("decoded_strings", [])
    stack = data.get("strings", {}).get("stack_strings", [])
    samples = decoded[:20] + stack[:10]
    for s in samples[:20]:
        add(
            findings,
            "info",
            "floss: decoded string",
            str(s)[:200],
            "Review the string for endpoints or keys.",
            "floss-string",
        )
    return {"status": "ok", "decoded": len(decoded), "stack": len(stack), "samples": samples[:20]}


def rizin(path: str, findings: list[dict], timeout: int) -> dict:
    if not have("rizin"):
        return {"status": "missing"}
    _code, out, err = run([tool("rizin"), "-q", "-j", "-c", "iI;iS;iE;ii;iz", path], timeout=timeout)
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return {"status": "failed", "error": err[:300]}
    imports = data.get("imports", []) or data.get("ii", [])
    strings = data.get("strings", []) or data.get("iz", [])
    funcs = data.get("functions", [])
    risky = {"strcpy", "strcat", "sprintf", "gets", "memcpy", "system", "popen", "execve", "recv", "read"}
    for imp in imports:
        name = imp.get("name", "") if isinstance(imp, dict) else str(imp)
        if name.split(".")[-1] in risky:
            add(findings, "info", "rizin: risky import", name, "Trace its arguments from input.", "rizin-import")
    if strings:
        add(
            findings,
            "info",
            "rizin: strings",
            f"{len(strings)} strings",
            "Review for endpoints and keys.",
            "rizin-strings",
        )
    return {"status": "ok", "imports": len(imports), "strings": len(strings), "functions": len(funcs)}


def ghidra(path: str, findings: list[dict], timeout: int, output: str) -> dict:
    home = os.environ.get("GHIDRA_HOME", "")
    analyze = os.path.join(home, "support", "analyzeHeadless") if home else ""
    if not analyze or not os.path.exists(analyze):
        return {"status": "missing", "hint": "set GHIDRA_HOME to the Ghidra install directory"}
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ghidra_dump.py")
    dump = output + ".ghidra.json"
    env = os.environ.copy()
    env["BERIL_GHIDRA_OUT"] = dump
    project = tempfile.mkdtemp(prefix="beril-ghidra-")
    cmd = [
        analyze,
        project,
        "beril",
        "-import",
        path,
        "-overwrite",
        "-postScript",
        script,
        "-scriptPath",
        os.path.dirname(script),
        "-deleteProject",
    ]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, env=env, errors="replace")
    except Exception as exc:
        return {"status": "failed", "error": str(exc)[:300]}
    if not os.path.exists(dump):
        return {"status": "failed", "error": (p.stderr or p.stdout)[-400:]}
    try:
        with open(dump, encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return {"status": "failed", "error": "dump not readable"}
    add(
        findings,
        "info",
        "ghidra: functions",
        str(len(data.get("functions", []))),
        "Open the project for review.",
        "ghidra-functions",
    )
    for item in data.get("suspicious", [])[:20]:
        add(findings, "info", "ghidra: suspicious call", item, "Check the data flow.", "ghidra-call")
    return {
        "status": "ok",
        "functions": len(data.get("functions", [])),
        "imports": len(data.get("imports", [])),
        "strings": len(data.get("strings", [])),
    }


def yara(path: str, findings: list[dict], rules: str, timeout: int) -> dict:
    if not rules or not have("yara"):
        return {"status": "missing" if not rules else "tool-missing"}
    _code, out, _err = run([tool("yara"), "-w", "-r", rules, path], timeout=timeout)
    hits = [line for line in out.splitlines() if line.strip()]
    for line in hits[:40]:
        add(findings, "medium", "YARA match", line, "Review the matched rule and offset.", "yara")
    return {"status": "ok", "matches": len(hits), "output": out[:2000]}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--capa", action="store_true")
    ap.add_argument("--floss", action="store_true")
    ap.add_argument("--rizin", action="store_true")
    ap.add_argument("--ghidra", action="store_true")
    ap.add_argument("--yara-rules", default="")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--tools", action="store_true", help="also run semgrep and gitleaks")
    args = ap.parse_args()

    base = scan_artifact.scan(args.target, use_tools=args.tools)
    findings = base.findings
    tools = {}
    if args.capa:
        tools["capa"] = capa(args.target, findings, args.timeout)
    if args.floss:
        tools["floss"] = floss(args.target, findings, args.timeout)
    if args.rizin:
        tools["rizin"] = rizin(args.target, findings, args.timeout)
    if args.ghidra:
        tools["ghidra"] = ghidra(args.target, findings, args.timeout, args.out or "/tmp/beril-re")
    if args.yara_rules:
        tools["yara"] = yara(args.target, findings, args.yara_rules, args.timeout)

    base.findings = findings
    base.meta["tools"] = tools
    base.finish()
    text = report_render.render_markdown(base, "engineer")
    if tools:
        text += "\n## Tool status\n\n"
        for name, status in tools.items():
            text += (
                f"- {name}: {status.get('status')}"
                + (f" ({status.get('error', '')[:160]})" if status.get("error") else "")
                + "\n"
            )
    print(base.to_json() if args.json else text)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        base.write_json(args.out + ".json")
        with open(args.out + ".md", "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"\nwrote {args.out}.md", file=sys.stderr)


if __name__ == "__main__":
    main()
