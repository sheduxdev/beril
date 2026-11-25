from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_front_desk_has_direct_triggers():
    text = (ROOT / "agents" / "front-desk.md").read_text(encoding="utf-8")
    assert "açık bul" in text
    assert "kır" in text
    assert "first tool call is a command" in text
    assert "--owned" in text


def test_router_points_at_front_desk():
    text = (ROOT / "agents" / "router.md").read_text(encoding="utf-8")
    assert "agents/front-desk.md" in text
    assert "Direct action" in text


def test_plugin_ships_the_natural_command():
    assert (ROOT / "plugin" / "claude-code" / "commands" / "do.md").exists()
    assert (ROOT / "plugin" / "claude-code" / "agents" / "beril-front-desk.md").exists()


def test_entry_files_mention_direct_action():
    for name in ("AGENTS.md", "CLAUDE.md", "GEMINI.md", "OPENAI.md"):
        text = (ROOT / name).read_text(encoding="utf-8").lower()
        assert "front-desk" in text or "front desk" in text, name
