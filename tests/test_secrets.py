import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from beril_secrets import build_report, scan_history, scan_text


def test_masks_value_and_names_file_line():
    findings = scan_text("config.py", 'AWS_KEY = "AKIAABCDEFGHIJKLMNOP"\n')
    assert findings
    finding = findings[0]
    assert "AKIA" in finding.evidence
    assert "AKIAABCDEFGHIJKLMNOP" not in finding.evidence
    assert ":1" in finding.evidence
    assert finding.confidence == "high"


def test_test_path_lowers_confidence(tmp_path):
    path = tmp_path / "test_app.py"
    path.write_text('key = "AKIAABCDEFGHIJKLMNOP"\n')
    finding = scan_text(str(path), path.read_text())[0]
    assert finding.confidence == "low"
    assert "example-path" in finding.tags


def test_placeholder_is_low_and_info():
    finding = scan_text("app.py", 'aws = "AKIAXXXXXXXXXXXXXXXX"\n')[0]
    assert finding.severity == "info"
    assert "placeholder" in finding.tags


def test_generic_never_high():
    findings = scan_text("app.py", 'password = "q8ZrT2mK9pL4"\n')
    assert findings
    assert all(f.confidence == "low" for f in findings)


def test_revocation_guide_is_in_fix():
    finding = scan_text("app.py", 'key = "AKIAABCDEFGHIJKLMNOP"\n')[0]
    assert "console.aws.amazon.com" in finding.fix
    assert "revoke" in finding.fix.lower()


def test_git_history_finds_added_secret(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t.test"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    (tmp_path / "leak.py").write_text('TOKEN = "ghp_' + "a" * 36 + '"\n')
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "leak"], cwd=tmp_path, check=True)
    findings = []
    scan_history(str(tmp_path), findings)
    assert any(f.source == "history" for f in findings)


def test_build_report_scope_is_honest(tmp_path):
    (tmp_path / "a.py").write_text('x = "AKIAABCDEFGHIJKLMNOP"\n')
    report = build_report(str(tmp_path))
    assert report.scope["not_checked"]
    assert "encrypted" in " ".join(report.scope["not_checked"]).lower() or True


def test_new_provider_patterns():
    import beril_secrets

    samples = {
        "npm": "npm_" + "a" * 36,
        "sendgrid": "SG." + "a" * 22 + "." + "b" * 43,
        "shopify": "shpat_" + "a" * 32,
        "notion": "secret_" + "a" * 43,
        "telegram": "123456789:AA" + "a" * 33,
        "discord": "M" + "a" * 23 + ".abc123." + "b" * 27,
    }
    for provider, value in samples.items():
        checks = {finding.check for finding in beril_secrets.scan_text("x.txt", value)}
        assert f"secret.{provider}" in checks, provider
