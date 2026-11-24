import glob
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import paths

ROOT = Path(__file__).resolve().parents[1]


def test_pyproject_license_is_an_expression():
    text = (ROOT / "pyproject.toml").read_text()
    assert 'license = "MIT"' in text
    assert "License ::" not in text


def test_data_files_exist_and_are_packaged():
    text = (ROOT / "pyproject.toml").read_text()
    block = text.split("[tool.setuptools.data-files]", 1)[1].split("\n[", 1)[0]
    patterns = re.findall(r'"(data/[^"]+|references/[^"]+|docs/[^"]+|agents/[^"]+)"', block)
    assert patterns
    for pattern in patterns:
        assert glob.glob(str(ROOT / pattern)), pattern


def test_action_uses_are_sha_pinned():
    for name in ("action.yml", "examples/github-action.yml"):
        text = (ROOT / name).read_text()
        refs = re.findall(r"uses:\s*(\S+)", text)
        assert refs
        for ref in refs:
            if ref.startswith("./"):
                continue
            assert re.search(r"@[0-9a-f]{40}$", ref), (name, ref)


def test_action_declares_the_contract():
    text = (ROOT / "action.yml").read_text()
    for key in ("target", "profile", "fail-on", "sarif", "json"):
        assert key in text
    assert 'default: "high"' in text


def test_dockerfile_pins_the_base_digest_and_drops_root():
    text = (ROOT / "Dockerfile").read_text()
    assert re.search(r"^ARG PYTHON_IMAGE=\S+@sha256:[0-9a-f]{64}", text, re.M)
    assert "USER 10001" in text


def test_workflow_matrix_covers_platforms_and_pythons():
    text = (ROOT / ".github/workflows/validate.yml").read_text()
    assert "ubuntu-latest" in text
    assert "macos-" in text
    assert "windows-latest" in text
    for version in ("3.11", "3.12", "3.13", "3.14"):
        assert f'"{version}"' in text


def test_workflow_exposes_the_catalog_check():
    text = (ROOT / ".github/workflows/validate.yml").read_text()
    assert "\n  catalog:\n" in text


def test_env_override_wins(monkeypatch, tmp_path):
    monkeypatch.setenv("BERIL_DATA", str(tmp_path))
    assert paths.locate("data", "BERIL_DATA") == str(tmp_path)


def test_share_prefix_is_found(monkeypatch, tmp_path):
    monkeypatch.delenv("BERIL_DATA", raising=False)
    empty = tmp_path / "empty"
    empty.mkdir()
    share = tmp_path / "share" / "beril" / "data"
    share.mkdir(parents=True)
    monkeypatch.setattr(paths, "HERE", str(empty))
    monkeypatch.setattr(sys, "prefix", str(tmp_path))
    assert paths.locate("data", "BERIL_DATA") == str(share)
