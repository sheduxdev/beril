import sys
from pathlib import Path
from typing import ClassVar

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import run


def test_select_url():
    tools, kind = run.select("https://a.test", [], [])
    assert kind == "web"
    assert "nuclei" in tools


def test_select_dir():
    tools, kind = run.select(".", [], [])
    assert kind == "source"
    assert "semgrep" in tools


def test_only_and_skip():
    tools, _ = run.select("https://a.test", ["nuclei", "testssl"], ["testssl"])
    assert tools == ["nuclei"]


def test_headers_from():
    class Args:
        auth_file: ClassVar[str] = ""
        header: ClassVar[list[str]] = ["X-Test: yes"]
        cookie: ClassVar[str] = "sid=1"

    headers = run.headers_from(Args())
    assert headers["X-Test"] == "yes"
    assert headers["Cookie"] == "sid=1"
