#!/usr/bin/env python3
"""Deliberately vulnerable web lab. Standard library only.

python labs/web/lab_server.py --port 8099
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
DB = sqlite3.connect(":memory:", check_same_thread=False)
DB.executescript("""
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, role TEXT, balance INTEGER);
CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT, price INTEGER);
INSERT INTO users VALUES (1, 'alice', 'alice@lab.local', 'user', 100);
INSERT INTO users VALUES (2, 'bob', 'bob@lab.local', 'user', 250);
INSERT INTO users VALUES (3, 'admin', 'admin@lab.local', 'admin', 9999);
INSERT INTO items VALUES (1, 'pistachio', 10);
INSERT INTO items VALUES (2, 'beryl', 120);
""")

PAGES = {
    "/": """<h1>Beril lab</h1>
<a href="/login?user=1">login as alice</a><br>
<a href="/profile?id=1">profile</a><br>
<a href="/search?q=pistachio">search</a><br>
<a href="/item?id=1">item</a><br>
<a href="/download?file=notes.txt">download</a><br>
<a href="/fetch?url=http://127.0.0.1:8099/health">fetch</a><br>
<a href="/admin">admin</a><br>
<a href="/api/users/1">api</a>""",
}


class Handler(BaseHTTPRequestHandler):
    server_version = "BerilLab/oops"

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"{self.address_string()} - " + (fmt % args))

    def send(
        self, body: str, code: int = 200, ctype: str = "text/html; charset=utf-8", headers: dict | None = None
    ) -> None:
        raw = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(raw)

    def cookie(self, name: str) -> str:
        raw = self.headers.get("Cookie", "")
        for part in raw.split(";"):
            k, _, v = part.strip().partition("=")
            if k == name:
                return v
        return ""

    def do_GET(self) -> None:
        parsed = urllib.parse.urlsplit(self.path)
        path, q = parsed.path, urllib.parse.parse_qs(parsed.query)

        if path == "/health":
            return self.send("ok", ctype="text/plain")
        if path == "/":
            return self.send(PAGES["/"])
        if path == "/login":
            uid = q.get("user", ["1"])[0]
            row = DB.execute("SELECT name, role FROM users WHERE id=?", (uid,)).fetchone()
            if not row:
                return self.send("no such user", 404)
            return self.send(f"hello {row[0]}", headers={"Set-Cookie": f"uid={uid}; Path=/, role={row[1]}; Path=/"})
        if path == "/profile":
            uid = q.get("id", ["1"])[0]
            row = DB.execute("SELECT id, name, email, balance FROM users WHERE id=?", (uid,)).fetchone()
            if not row:
                return self.send("not found", 404)
            return self.send(f"<h1>Profile</h1><p>{row[1]} | {row[2]} | balance {row[3]}</p>")
        if path == "/search":
            needle = q.get("q", [""])[0]
            return self.send(f"<h1>Search</h1><p>You searched for: {needle}</p>")
        if path == "/item":
            uid = q.get("id", ["1"])[0]
            try:
                row = DB.execute(f"SELECT id, name, price FROM items WHERE id={uid}").fetchone()
            except sqlite3.Error as exc:
                return self.send(f"SQL error: {exc}", 500)
            if not row:
                return self.send("item not found", 404)
            return self.send(f"<h1>{row[1]}</h1><p>price {row[2]}</p>")
        if path == "/download":
            name = q.get("file", ["notes.txt"])[0]
            full = os.path.join(ROOT, name)
            try:
                return self.send(open(full, encoding="utf-8", errors="replace").read(), ctype="text/plain")
            except OSError as exc:
                return self.send(f"cannot read {full}: {exc}", 404)
        if path == "/fetch":
            url = q.get("url", [""])[0]
            try:
                body = urllib.request.urlopen(url, timeout=5).read().decode("utf-8", "replace")
                return self.send(f"<h1>Fetched</h1><pre>{body[:2000]}</pre>")
            except Exception as exc:
                return self.send(f"fetch failed: {exc}", 502)
        if path == "/admin":
            if self.cookie("role") != "admin":
                return self.send("forbidden: role cookie is " + (self.cookie("role") or "none"), 403)
            return self.send("<h1>Admin</h1><p>secret: PISTACHIO-ADMIN-42</p>")
        if path.startswith("/api/users/"):
            uid = path.rsplit("/", 1)[-1]
            row = DB.execute("SELECT id, name, email, role, balance FROM users WHERE id=?", (uid,)).fetchone()
            if not row:
                return self.send(json.dumps({"error": "not found"}), 404, "application/json")
            return self.send(
                json.dumps({"id": row[0], "name": row[1], "email": row[2], "role": row[3], "balance": row[4]}),
                ctype="application/json",
            )
        if path == "/api/transfer":
            return self.send(json.dumps({"ok": True, "from": 1, "to": 2, "amount": 10}), ctype="application/json")
        return self.send("not found", 404)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8099)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"lab on http://{args.host}:{args.port}")
    srv.serve_forever()


if __name__ == "__main__":
    main()
