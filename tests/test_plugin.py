import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import install_plugin


def test_install_claude(tmp_path):
    files = install_plugin.install("claude", tmp_path, True)
    assert files
    target = Path(files[0])
    assert (target / ".claude-plugin" / "plugin.json").exists()
    assert (target / "commands" / "scan.md").exists()


def test_install_all(tmp_path):
    for agent in ("codex", "gemini"):
        install_plugin.install(agent, tmp_path, True)
    assert (tmp_path / ".codex" / "beril" / "AGENTS.md").exists()
    assert (tmp_path / ".gemini" / "extensions" / "beril" / "gemini-extension.json").exists()
