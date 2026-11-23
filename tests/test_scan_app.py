import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scan_app


def test_passive_needs_no_gate(web_app, auth_store):
    report = scan_app.scan(web_app, mode="passive", rate=10, max_requests=150)
    assert report.mode == "passive"
    assert report.authorization == {}
    assert report.findings


def test_active_without_auth_exits(web_app, auth_store):
    with pytest.raises(SystemExit) as exc:
        scan_app.scan(web_app, mode="active", rate=10)
    assert "authorization" in str(exc.value)


def test_active_with_owned_finds_probes(web_app, auth_store):
    report = scan_app.scan(web_app, mode="active", owned=True, rate=10, max_requests=200)
    checks = {f.check for f in report.findings}
    assert "active.traversal" in checks
    assert "active.xss.reflect" in checks or "active.sqli.error" in checks
    assert "web.path.env" in checks
    assert "web.path.git-head" in checks
    assert report.authorization["method"] == "ack"


def test_active_scope_file_blocks_other_host(web_app, auth_store, tmp_path):
    scope = tmp_path / "scope.txt"
    scope.write_text("other.example\n")
    with pytest.raises(SystemExit):
        scan_app.scan(web_app, mode="active", owned=True, scope_file=str(scope), rate=10)


def test_budget_is_reported(web_app, auth_store):
    report = scan_app.scan(web_app, mode="passive", rate=10, max_requests=3)
    assert report.limits["requests_sent"] <= 3
    assert any("budget" in e for e in report.errors)


def test_robots_disallow_is_recorded(web_app, auth_store):
    report = scan_app.scan(web_app, mode="passive", rate=10, max_requests=60)
    assert report.limits["robots"] == "respected"


def test_headers_and_cookies_are_findings(web_app, auth_store):
    report = scan_app.scan(web_app, mode="passive", rate=10, max_requests=60)
    checks = {f.check for f in report.findings}
    assert any("content-security-policy" in c for c in checks)
    assert any("cookie" in c for c in checks)


def test_extra_headers_are_sent(web_app, auth_store):
    report = scan_app.scan(f"{web_app}/auth", rate=10, max_requests=5, headers={"X-Test": "yes"})
    assert report.meta["status"] == 200


def test_render_sets_mode(web_app, auth_store):
    report = scan_app.scan(web_app, rate=10, max_requests=20, render=True)
    assert report.meta["render"] == "camoufox"
    assert report.meta["status"] == 200
