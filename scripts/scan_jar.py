#!/usr/bin/env python3
"""Static triage for a JAR, a Minecraft plugin or a mods/plugins folder.

Never executes the JAR. Reads the zip, the manifest, the class constant pool
strings and a small IOC set. Reports behavior leads with confidence, so a
reviewer can decide what to open in a decompiler.

    python scripts/scan_jar.py --target ./plugins
    python scripts/scan_jar.py --target ./FreeRank.jar --out scans/freerank
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import re
import sys
import zipfile
from pathlib import Path

import fileio
import paths
from beril_model import Finding, Report

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MAX_MEMBER = 4_000_000
MAX_CLASSES = 20_000
MAX_TOTAL = 300_000_000
SUSPICIOUS_CLASS = re.compile(
    r"\b(Runtime|ProcessBuilder|URLClassLoader|ClassLoader|MessageDigest|Cipher|"
    r"Base64|HttpURLConnection|Socket|setOp|defineClass)\b"
)
B64 = re.compile(r"\b[A-Za-z0-9+/]{80,}={0,2}\b")
URL = re.compile(r"https?://[^\s'\"<>\x00]{6,200}")
OBFUSCATED = re.compile(r"^[a-zA-Z]{1,3}$")


def load_iocs() -> dict:
    try:
        with open(os.path.join(paths.DATA, "jar_iocs.json"), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError):
        return {"files": [], "strings": [], "known_sha256": {}, "plugins": []}


def sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1_000_000), b""):
            digest.update(chunk)
    return digest.hexdigest()


def strings_of(raw: bytes) -> list[str]:
    return [m.group().decode("utf-8", "replace") for m in re.finditer(rb"[\x20-\x7e]{6,}", raw)]


def scan_one(path: str) -> list[Finding]:
    findings: list[Finding] = []
    iocs = load_iocs()
    digest = sha256(path)
    name = os.path.basename(path)
    findings.append(
        Finding(
            check="jar.hash",
            title="JAR parmak izi",
            severity="info",
            confidence="high",
            evidence=f"{path}: sha256 {digest}",
            impact="Identifies the same file on other machines.",
            fix="Compare it with a known-good hash list.",
            subject=path,
            source="static",
            tags=["hash"],
            false_positive="A hash alone says nothing about intent.",
        )
    )
    if digest in iocs.get("known_sha256", {}):
        findings.append(
            Finding(
                check="jar.known-bad",
                title="Known bad hash",
                severity="critical",
                confidence="high",
                evidence=f"{path}: {digest} = {iocs['known_sha256'][digest]}",
                impact="Same file as a previously reported malicious sample.",
                fix="Remove the JAR, revoke tokens and verify the server with a clean build.",
                subject=path,
                source="static",
                tags=["known-bad"],
            )
        )
    if digest in iocs.get("known_good_sha256", {}):
        findings.append(
            Finding(
                check="jar.known-good",
                title="Hash matches a pinned distribution",
                severity="info",
                confidence="high",
                evidence=f"{path}: {digest} = {iocs['known_good_sha256'][digest]}",
                impact="The file is the one published for that version.",
                fix="Still review the plugin list and the update source.",
                subject=path,
                source="static",
                tags=["known-good"],
                false_positive="A rebuilt or patched file has another hash.",
            )
        )
    try:
        zf = zipfile.ZipFile(path)
    except zipfile.BadZipFile:
        return [
            Finding(
                check="jar.invalid",
                title="JAR cannot be read",
                severity="medium",
                confidence="high",
                evidence=path,
                impact="The file is corrupt or not a JAR.",
                fix="Download it again.",
                subject=path,
            )
        ]
    with zf:
        names = zf.namelist()
        infos = zf.infolist()
        # Manifest and plugin.yml
        for meta in ("plugin.yml", "paper-plugin.yml", "bungee.yml", "META-INF/MANIFEST.MF"):
            if meta in names and zf.getinfo(meta).file_size < 200_000:
                text = zf.read(meta).decode("utf-8", "replace")
                findings += check_manifest(path, meta, text, name, iocs)
        # IOC files and hidden entries
        for entry in names:
            base = entry.rsplit("/", 1)[-1]
            if base in iocs.get("files", []):
                findings.append(
                    Finding(
                        check="jar.ioc-file",
                        title=f"Known IOC file: {base}",
                        severity="high",
                        confidence="high",
                        evidence=f"{path}: {entry}",
                        impact="A file name left by a Minecraft malware family.",
                        fix="Read the contents and revoke tokens if the family matches.",
                        subject=f"{path}:{entry}",
                        source="static",
                        tags=["ioc"],
                    )
                )
            if base.startswith(".") and base not in (".", "..") and not base.startswith(".git"):
                findings.append(
                    Finding(
                        check="jar.hidden-file",
                        title=f"Hidden file: {base}",
                        severity="low",
                        confidence="medium",
                        evidence=f"{path}: {entry}",
                        impact="May be a hidden payload or config.",
                        fix="Extract and read it.",
                        subject=f"{path}:{entry}",
                        source="static",
                    )
                )
            if entry.endswith((".jar", ".zip")) and entry != name:
                findings.append(
                    Finding(
                        check="jar.nested",
                        title="Archive embedded in the JAR",
                        severity="info",
                        confidence="high",
                        evidence=f"{path}: {entry}",
                        impact="Nested packages get missed.",
                        fix="Extract and scan it separately.",
                        subject=f"{path}:{entry}",
                        source="static",
                    )
                )
        # Class strings
        hits = collections.Counter()
        urls: list[str] = []
        b64 = 0
        strings = 0
        class_names = []
        total = 0
        for info in infos:
            if not info.filename.endswith(".class") or info.file_size > MAX_MEMBER:
                continue
            if len(class_names) >= MAX_CLASSES or total >= MAX_TOTAL:
                break
            class_names.append(info.filename)
            total += info.file_size
            try:
                raw = zf.read(info)
            except Exception:
                continue
            for value in strings_of(raw):
                strings += 1
                if URL.match(value):
                    urls.append(value)
                if B64.match(value):
                    b64 += 1
                for rule in iocs.get("strings", []):
                    if rule["needle"] in value:
                        hits[rule["needle"]] += 1
        for rule in iocs.get("strings", []):
            count = hits.get(rule["needle"], 0)
            if not count:
                continue
            confidence = "high" if count >= 2 else "medium"
            findings.append(
                Finding(
                    check="jar.string." + re.sub(r"\W+", "-", rule["needle"]).strip("-").lower(),
                    title=f"Behavior hint: {rule['label']}",
                    severity=rule["severity"],
                    confidence=confidence,
                    evidence=f"{path}: {count} classes contain {rule['needle']}",
                    impact="This API group can load code, run commands or call out.",
                    fix="Decompile the class and read the call chain and target URL.",
                    subject=path,
                    source="static",
                    tags=["behavior"],
                    false_positive="Every plugin can use these APIs for legitimate work.",
                )
            )
        unique_urls = sorted(set(urls))
        if unique_urls:
            findings.append(
                Finding(
                    check="jar.urls",
                    title=f"External URLs ({len(unique_urls)})",
                    severity="medium",
                    confidence="high",
                    evidence=", ".join(unique_urls[:8])[:500],
                    impact="Content or commands can arrive at run time.",
                    fix="Check ownership and integrity, and pin a version.",
                    subject=path,
                    source="static",
                    tags=["network"],
                    false_positive="Update and stats endpoints show up here too.",
                )
            )
        if b64:
            findings.append(
                Finding(
                    check="jar.base64",
                    title="Long Base64 blocks",
                    severity="low",
                    confidence="medium",
                    evidence=f"{path}: {b64} blok",
                    impact="A class or config may be hidden.",
                    fix="Decode the blocks and check whether a class is loaded.",
                    subject=path,
                    source="static",
                    false_positive="Assets and images can be Base64 too.",
                )
            )
        if class_names:
            simple = [c.rsplit("/", 1)[-1].replace(".class", "") for c in class_names]
            obf = sum(1 for s in simple if OBFUSCATED.match(s))
            ratio = obf / max(len(simple), 1)
            if ratio > 0.5 and len(simple) > 10:
                findings.append(
                    Finding(
                        check="jar.obfuscated",
                        title="Heavy obfuscation",
                        severity="medium",
                        confidence="medium",
                        evidence=f"{path}: {ratio * 100:.0f}% of class names are short",
                        impact="Reading and IOC matching get harder, and malware can hide.",
                        fix="Recover names with a decompiler and extract strings.",
                        subject=path,
                        source="static",
                        false_positive="Commercial plugins shrink code too.",
                    )
                )
        stamps = [i.date_time for i in infos if i.date_time]
        if stamps:
            newest = max(stamps)
            recent = sum(1 for s in stamps if s[:3] == newest[:3])
            if len(stamps) > 20 and recent == len(stamps):
                findings.append(
                    Finding(
                        check="jar.timestamps",
                        title="All entries share one minute",
                        severity="info",
                        confidence="low",
                        evidence=f"{path}: {len(stamps)} girdi, {newest}",
                        impact="Repackaging is likely. The original build time is gone.",
                        fix="Compare the hash with the original distribution.",
                        subject=path,
                        source="static",
                    )
                )
    return findings


def check_manifest(path: str, meta: str, text: str, filename: str, iocs: dict) -> list[Finding]:
    out = []
    if meta != "plugin.yml" and meta != "paper-plugin.yml" and meta != "bungee.yml":
        return out
    name = re.search(r"^name:\s*(.+)$", text, re.M)
    version = re.search(r"^version:\s*(.+)$", text, re.M)
    main = re.search(r"^main:\s*(.+)$", text, re.M)
    if name and main:
        declared = name.group(1).strip()
        if declared.lower().replace(" ", "-") not in filename.lower():
            out.append(
                Finding(
                    check="jar.manifest-mismatch",
                    title="plugin.yml name does not match the file name",
                    severity="medium",
                    confidence="medium",
                    evidence=f"{path}: name '{declared}', file '{filename}', main '{main.group(1).strip()}'",
                    impact="The plugin may be cloned or repacked.",
                    fix="Compare author and version with the original source.",
                    subject=path,
                    source="static",
                    false_positive="Rebranding can be legitimate.",
                )
            )
    if main and not re.match(r"^[\w.]+$", main.group(1).strip()):
        out.append(
            Finding(
                check="jar.main-class",
                title="Suspicious main class",
                severity="low",
                confidence="medium",
                evidence=f"{path}: {main.group(1).strip()}",
                impact="The class name is out of package or oddly formed.",
                fix="Decompile the class.",
                subject=path,
                source="static",
            )
        )
    if version and re.search(r"(?i)(snapshot|dev|test|1\.0$)", version.group(1)):
        out.append(
            Finding(
                check="jar.version",
                title="Development-looking version",
                severity="low",
                confidence="low",
                evidence=f"{path}: version {version.group(1).strip()}",
                impact="Version tracking and updates get harder.",
                fix="Use a pinned version.",
                subject=path,
                source="static",
            )
        )
    if "author" not in text.lower():
        out.append(
            Finding(
                check="jar.no-author",
                title="No author in plugin.yml",
                severity="info",
                confidence="high",
                evidence=path,
                impact="Source validation is hard.",
                fix="Keep the author and repository in plugin.yml.",
                subject=path,
                source="static",
            )
        )
    return out


def scan(target: str, out_prefix: str = "") -> Report:
    p = Path(target)
    jars = [str(p)] if p.is_file() else sorted(str(x) for x in p.rglob("*.jar"))[:500]
    report = Report(target=target, mode="jar")
    report.scope["checked"] = [
        "JAR manifest and plugin.yml",
        "Class strings",
        "IOC file names",
        "Embedded archives",
        "Hash",
        "Timestamps",
        "Obfuscation ratio",
    ]
    report.scope["not_checked"] = [
        "Class bytecode semantics",
        "Runtime behavior",
        "Signature validation",
        "Known bad hash database (local seed)",
    ]
    if not jars:
        report.errors.append("No JAR found")
        return report.finish()
    for jar in jars:
        for finding in scan_one(jar):
            report.add(finding)
    report.finish()
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if not os.path.exists(args.target):
        sys.exit(f"not found: {args.target}")
    report = scan(args.target)
    text = report.to_json() if args.json else render(report)
    print(text)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        fileio.write_json(args.out + ".json", report.to_dict())
        fileio.write_text(args.out + ".md", render(report) + "\n")


def render(report: Report) -> str:
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    lines = [f"# JAR triage: {report.target}", "", f"{len(report.findings)} findings. Static, nothing executed.", ""]
    for f in sorted(report.findings, key=lambda x: order.get(x.severity, 9)):
        lines += [f"- [{f.severity}/{f.confidence}] {f.title}: {f.evidence}"]
    lines += [
        "",
        "## Limits",
        "",
        "A behavior hint does not convict a plugin. Decompile the class and read the call chain.",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    main()
