import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import deps
import scan_artifact
import source_audit


def test_offline_dep_hit_and_reachability(tmp_path):
    (tmp_path / "package-lock.json").write_text(
        json.dumps({"packages": {"": {}, "node_modules/lodash": {"version": "4.17.20"}}})
    )
    (tmp_path / "app.js").write_text("const _ = require('lodash');\n")
    report = deps.scan(str(tmp_path), do_reach=True)
    finding = next(f for f in report.findings if "lodash" in f.title)
    assert finding.severity == "high"
    assert "reachable" in finding.impact


def test_unused_dep_is_low_confidence(tmp_path):
    (tmp_path / "package-lock.json").write_text(
        json.dumps({"packages": {"": {}, "node_modules/lodash": {"version": "4.17.20"}}})
    )
    (tmp_path / "app.js").write_text("console.log('x')\n")
    report = deps.scan(str(tmp_path), do_reach=True)
    finding = next(f for f in report.findings if "lodash" in f.title)
    assert finding.confidence == "low"


def test_version_compare():
    assert deps.version_lt("4.17.20", "4.17.21")
    assert not deps.version_lt("4.17.21", "4.17.20")
    assert deps.version_lt("1.0.0", "10.0.0")


def test_source_rule_tls_off(tmp_path):
    path = tmp_path / "a.py"
    path.write_text("import requests\nrequests.get('https://x', verify=False)\n")
    findings = source_audit.scan_text("a.py", path.read_text(), "python")
    assert any(f.check == "src.tls-verify-off" for f in findings)


def test_fan_in_flags_shared_module():
    files = {f"m{i}.py": "from helpers import x\n" for i in range(12)}
    files["helpers.py"] = "def x(): pass\n"
    findings = source_audit.fan_in(files)
    assert findings
    assert findings[0].check == "src.fan-in"


def test_artifact_masks_secret(tmp_path):
    (tmp_path / "config.py").write_text('AWS_KEY = "AKIAABCDEFGHIJKLMNOP"\n')
    report = scan_artifact.scan(str(tmp_path))
    text = report.to_json()
    assert "AKIAABCDEFGHIJKLMNOP" not in text
    assert "secret.aws" in text


def test_c_and_java_rules_fire():
    import source_audit

    c_checks = {f.check for f in source_audit.scan_text("a.c", "char b[8]; gets(b); system(cmd);", "c")}
    assert {"src.c-gets", "src.c-system"} <= c_checks
    java = 'Statement s = c.createStatement(); s.executeQuery("select " + id);'
    assert "src.java-sql-concat" in {f.check for f in source_audit.scan_text("A.java", java, "java")}


def test_ssrf_and_csrf_rules():
    import source_audit

    checks = {f.check for f in source_audit.scan_text("a.py", 'requests.get(request.args["u"])', "python")}
    assert "src.ssrf-url-from-request" in checks
    checks = {f.check for f in source_audit.scan_text("b.py", "csrf().disable()", "python")}
    assert "src.csrf-disabled" in checks
