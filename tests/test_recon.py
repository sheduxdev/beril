import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import recon


def data():
    return json.loads((Path(__file__).resolve().parents[1] / "data" / "recon.json").read_text())


def test_normalize_domain():
    assert recon.normalize_domain("https://Example.COM:8443/a/b") == "example.com"
    assert recon.normalize_domain("example.com.") == "example.com"


def test_valid_domain():
    assert recon.valid_domain("example.com")
    assert recon.valid_domain("a-b.example.co.uk")
    assert not recon.valid_domain("bad_domain.example")
    assert not recon.valid_domain("")


def test_private_and_cdn():
    ranges = data()["cdn_ranges"]
    assert recon.ip_private("10.0.0.5")
    assert recon.ip_private("127.0.0.1")
    assert recon.cdn_name("104.16.1.1", ranges) == "cloudflare"
    assert recon.cdn_name("8.8.8.8", ranges) == ""


def test_fingerprint_matches_header_and_body():
    seed = data()
    observation = {
        "headers": {"server": "nginx/1.24.0", "set-cookie": "laravel_session=abc"},
        "body": "<html><link href='/bootstrap.min.css'></html>",
        "title": "App",
    }
    hits = {item["name"] for item in recon.fingerprint(observation, seed)}
    assert "nginx" in hits
    assert "Laravel" in hits
    assert "Bootstrap" in hits
    nginx = next(item for item in recon.fingerprint(observation, seed) if item["name"] == "nginx")
    assert nginx["version"] == "1.24.0"


def test_takeover_requires_marker_or_404():
    seed = data()
    with_marker = {
        "body": "There isn't a GitHub Pages site here",
        "http_status": 404,
        "https_status": 0,
    }
    hits = recon.takeover_matches(with_marker, ["user.github.io"], seed, set())
    assert hits and hits[0]["service"] == "GitHub Pages"
    assert hits[0]["confidence"] == "high"

    without_marker = {"body": "something else", "http_status": 404, "https_status": 0}
    hits = recon.takeover_matches(without_marker, ["user.github.io"], seed, set())
    assert hits and hits[0]["confidence"] == "medium"

    hits = recon.takeover_matches({"body": "x", "http_status": 200}, ["user.github.io"], seed, {"user.github.io"})
    assert hits and hits[0]["confidence"] == "medium"

    hits = recon.takeover_matches({"body": "x", "http_status": 200}, ["user.github.io"], seed, set())
    assert hits == []


def test_dangling_cnames(monkeypatch):
    seed = data()
    monkeypatch.setattr(recon, "resolve_host", lambda host: ([], []) if host == "gone.github.io" else (["1.2.3.4"], []))
    assert recon.dangling(["gone.github.io", "live.github.io", "cdn.example.net"], seed) == {"gone.github.io"}


def test_score_ranks_admin_over_blog():
    admin = {"host": "admin.example.com", "http_status": 200, "https_status": 200}
    blog = {"host": "blog.example.com", "http_status": 200, "https_status": 200}
    admin_score, admin_risk, _ = recon.score_host(admin, [], data())
    blog_score, _, _ = recon.score_host(blog, [], data())
    assert admin_score > blog_score
    assert admin_risk in ("critical", "high")


def test_origin_filters_cdn_and_private(monkeypatch):
    seed = data()
    monkeypatch.setattr(recon, "dig", lambda *args, **kwargs: [])
    monkeypatch.setattr(recon, "resolve_host", lambda host: ([], []))
    monkeypatch.setattr(recon, "responds", lambda ip: ip == "1.2.3.4")
    observations = [{"ip": "1.2.3.4", "headers": {"x-forwarded-for": "1.2.3.4, 10.0.0.1"}}]
    ranked, apex_cdn = recon.origin_candidates(
        "example.com",
        ["104.16.1.1"],
        observations,
        set(),
        seed,
        seed["cdn_ranges"],
    )
    assert apex_cdn is True
    assert [item["ip"] for item in ranked] == ["1.2.3.4"]
    assert "http_header" in ranked[0]["methods"]


def test_end_to_end_with_stubs(monkeypatch, auth_store, tmp_path):
    monkeypatch.setattr(recon, "load_data", data)
    monkeypatch.setattr(
        recon, "enumerate_subdomains", lambda *args: ({"admin.example.com", "www.example.com"}, {"crtsh": 2}, [])
    )
    monkeypatch.setattr(recon, "subdomain_score", lambda host, d: 50 if host.startswith("admin") else 0)
    monkeypatch.setattr(recon, "dig", lambda *args, **kwargs: [])
    monkeypatch.setattr(recon, "responds", lambda ip: True)
    monkeypatch.setattr(recon, "auth_surface", lambda *args: {"login": ["https://example.com/login"], "reset": []})
    monkeypatch.setattr(recon, "emails_on", lambda *args: ["security@example.com"])

    def fake_resolve(host):
        if host == "example.com":
            return ["93.184.216.34"], ["edge.cloudflare.net"]
        if host == "admin.example.com":
            return ["1.2.3.4"], ["old.github.io"]
        return ["93.184.216.34"], []

    monkeypatch.setattr(recon, "resolve_host", fake_resolve)

    def fake_probe(fetcher, host):
        if host == "admin.example.com":
            return {
                "host": host,
                "http_status": 200,
                "https_status": 0,
                "title": "Admin",
                "server": "nginx",
                "powered_by": "PHP",
                "headers": {"server": "nginx", "x-forwarded-for": "1.2.3.4"},
                "body": "There isn't a GitHub Pages site here",
                "url": "http://admin.example.com/",
            }
        return {
            "host": host,
            "http_status": 200,
            "https_status": 200,
            "title": "Home",
            "server": "nginx",
            "powered_by": "",
            "headers": {"server": "nginx"},
            "body": "<html>home</html>",
            "url": "https://example.com/",
        }

    monkeypatch.setattr(recon, "http_probe", fake_probe)
    report = recon.recon("example.com", rate=1000, max_requests=50, max_hosts=10, bruteforce=False, sources=[])
    checks = {finding.check for finding in report.findings}
    assert "recon.takeover" in checks
    assert "recon.high-value-host" in checks
    assert "recon.auth.login" in checks
    assert "recon.emails" in checks
    assert "recon.https-missing" in checks
    inventory = report.meta["inventory"]
    assert inventory[0]["host"] == "admin.example.com"
    assert inventory[0]["category"] == "admin"


def test_markdown_has_no_crash():
    report = recon.Report(target="example.com", mode="passive")
    report.scope["checked"] = ["x"]
    report.scope["not_checked"] = ["y"]
    report.finish()
    text = recon.markdown(report, [], [], {"login": [], "reset": []}, [], False)
    assert "# Recon: example.com" in text
    assert "Host inventory" in text
