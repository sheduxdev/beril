import json
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import priority  # noqa: E402
import sbom  # noqa: E402
import scan_artifact  # noqa: E402


def test_priority_seed_marks_kev():
    data = priority.enrich("CVE-2021-44228")
    assert data["kev"] is True
    assert data["epss"] is not None


def test_priority_unknown_cve():
    data = priority.enrich("CVE-2099-99999")
    assert data["kev"] is False


def test_archive_traversal_finding(tmp_path):
    path = tmp_path / "a.zip"
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("../evil.txt", "x")
        zf.writestr("ok.txt", "y")
    report = scan_artifact.scan(str(path))
    assert "zip-traversal" in {f.check for f in report.findings}


def test_jar_routes_through_artifact(tmp_path):
    path = tmp_path / "p.jar"
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("plugin.yml", "name: A\nversion: 1.0\nmain: a.Main\n")
    report = scan_artifact.scan(str(path))
    assert report.mode == "jar"
    assert any(f.check == "jar.hash" for f in report.findings)


def test_sbom_purl_and_license(tmp_path):
    (tmp_path / "package-lock.json").write_text(
        json.dumps({"packages": {"": {}, "node_modules/lodash": {"version": "4.17.20"}}})
    )
    (tmp_path / "LICENSE").write_text("MIT License\n")
    data = sbom.build(str(tmp_path))
    component = data["components"][0]
    assert component["purl"] == "pkg:npm/lodash@4.17.20"
    assert "licenses" not in component
    assert data["metadata"]["component"]["licenses"][0]["license"]["name"] == "MIT"


def test_report_cli_roundtrip(tmp_path, web_app):
    scan = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/scan_app.py"),
            "--target",
            web_app,
            "--json",
            "--out",
            str(tmp_path / "s"),
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert scan.returncode == 0, scan.stderr
    data = json.loads((tmp_path / "s.json").read_text())
    assert data["schema"] == "beril.report/1"
    out = tmp_path / "smb.md"
    render = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/report_render.py"),
            "--input",
            str(tmp_path / "s.json"),
            "--profile",
            "smb",
            "--out",
            str(out),
        ],
        capture_output=True,
        text=True,
    )
    assert render.returncode == 0, render.stderr
    text = out.read_text()
    assert "KVKK" in text
    assert "Checks not attempted" in text


def test_sarif_has_file_location(tmp_path):
    import report_render
    from beril_model import Finding, Report

    report = Report(target=str(tmp_path))
    report.add(
        Finding(
            check="src.eval-exec",
            title="eval",
            severity="medium",
            confidence="low",
            evidence="a.py:3 eval(",
            impact="x",
            fix="y",
            subject="a.py:3",
        )
    )
    doc = json.loads(report_render.render_sarif(report))
    location = doc["runs"][0]["results"][0]["locations"][0]["physicalLocation"]
    assert location["artifactLocation"]["uri"] == "a.py"
    assert location["region"]["startLine"] == 3


def test_fail_on_and_baseline(tmp_path, web_app):
    first = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/scan_app.py"),
            "--target",
            web_app,
            "--json",
            "--out",
            str(tmp_path / "base"),
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert first.returncode == 0, first.stderr
    gate = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/scan_app.py"),
            "--target",
            web_app,
            "--json",
            "--out",
            str(tmp_path / "gate"),
            "--fail-on",
            "critical",
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert gate.returncode == 1
    second = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/scan_app.py"),
            "--target",
            web_app,
            "--json",
            "--out",
            str(tmp_path / "second"),
            "--baseline",
            str(tmp_path / "base.json"),
            "--fail-on",
            "critical",
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert second.returncode == 0, second.stderr
    data = json.loads((tmp_path / "second.json").read_text())
    assert data["counts"]["critical"] == 0
    assert data["meta"]["suppressed"] > 0
