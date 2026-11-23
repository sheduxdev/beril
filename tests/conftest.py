"""Shared fixtures: a deliberately messy local web app."""

from __future__ import annotations

import threading
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest


class Handler(BaseHTTPRequestHandler):
    server_version = "BerilTest/1.0"

    def log_message(self, *args):
        pass

    def send(
        self, body: str | bytes, code: int = 200, ctype: str = "text/html; charset=utf-8", headers: dict | None = None
    ):
        raw = body.encode() if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        parts = urllib.parse.urlsplit(self.path)
        path, query = parts.path, urllib.parse.parse_qs(parts.query)
        if path == "/auth":
            if self.headers.get("X-Test") == "yes":
                return self.send("authorized")
            return self.send("denied", 401)
        if path == "/":
            return self.send(
                '<html><title>Test</title><form><input type="password"></form>'
                '<a href="/search?q=hello">s</a><a href="/item?id=1">i</a>'
                '<a href="/download?file=notes.txt">d</a><a href="/redirect?next=/x">r</a>'
                '<meta name="generator" content="WordPress 6.0"></html>',
                headers={"Set-Cookie": "sid=abc; Path=/"},
            )
        if path == "/search":
            return self.send(f"<h1>Result</h1><p>{query.get('q', [''])[0]}</p>")
        if path == "/item":
            value = query.get("id", ["1"])[0]
            if "'" in value:
                return self.send('SQL error: near "\'": syntax error', 500)
            return self.send("<h1>item</h1>")
        if path == "/download":
            name = query.get("file", ["notes.txt"])[0]
            import os

            root = os.path.dirname(os.path.abspath(__file__))
            full = os.path.join(root, name)
            if "etc/passwd" in name:
                return self.send("root:x:0:0:root:/root:/bin/bash\n", ctype="text/plain")
            if os.path.exists(full):
                return self.send(open(full, encoding="utf-8").read(), ctype="text/plain")
            return self.send("missing", 404)
        if path == "/redirect":
            target = query.get("next", ["/"])[0]
            if target.startswith("//"):
                target = "https:" + target
            return self.send("", 302, headers={"Location": target})
        if path == "/login":
            return self.send("ok", headers={"Set-Cookie": "sid=abc; Path=/"})
        if path == "/.env":
            return self.send("DB_PASSWORD=hunter2\nAPI_KEY=sk_live_TEST1234567890abcd\n", ctype="text/plain")
        if path == "/.git/HEAD":
            return self.send("ref: refs/heads/main\n", ctype="text/plain")
        if path == "/backup.zip":
            return self.send(b"PK\x03\x04fake", ctype="application/zip")
        if path == "/robots.txt":
            return self.send("User-agent: *\nDisallow: /admin\nDisallow: /backup\n", ctype="text/plain")
        if path == "/admin":
            return self.send("forbidden", 403)
        if path == "/.well-known/security.txt":
            return self.send("Contact: mailto:sec@example.test\n", ctype="text/plain")
        return self.send("not found", 404)


@pytest.fixture()
def web_app():
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_address[1]}"
    server.shutdown()
    server.server_close()


@pytest.fixture()
def auth_store(tmp_path, monkeypatch):
    import authz

    monkeypatch.setattr(authz, "STORE", str(tmp_path / "authz"))
    return tmp_path / "authz"
