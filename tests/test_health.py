import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import project_health


def make_repo(tmp_path):
    (tmp_path / "README.md").write_text("# Project\n" + "x" * 5000)
    (tmp_path / "LICENSE").write_text("MIT License\n")
    (tmp_path / "SECURITY.md").write_text("Report privately.\n")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_x.py").write_text("def test_x():\n    assert True\n")
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    (tmp_path / ".github" / "workflows" / "ci.yml").write_text("on: push\n")
    (tmp_path / "package-lock.json").write_text(json.dumps({"packages": {}}))
    for args in (("init", "-q"), ("add", "."), ("-c", "user.email=a@b", "-c", "user.name=a", "commit", "-qm", "x")):
        subprocess.run(["git", *args], cwd=tmp_path, check=True)


def test_scorecard_has_every_dimension(tmp_path):
    make_repo(tmp_path)
    report, scores = project_health.inspect(str(tmp_path))
    assert set(scores) == set(project_health.DIMENSIONS)
    assert all(0 <= value <= 100 for value in scores.values())
    assert report.meta["signals"]["tests"] is True
    assert "health.no-tests" not in {finding.check for finding in report.findings}


def test_missing_files_are_flagged(tmp_path):
    (tmp_path / "README.md").write_text("# Empty\n")
    report, _ = project_health.inspect(str(tmp_path))
    checks = {finding.check for finding in report.findings}
    assert {"health.no-tests", "health.no-ci", "health.no-security-file", "health.no-license"} <= checks


def test_missing_target_is_an_error(tmp_path):
    report, _ = project_health.inspect(str(tmp_path / "nope"))
    assert report.errors
