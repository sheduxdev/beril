#!/usr/bin/env python3
"""Deliberately broken API lab. Standard library only, local only.

    python labs/api/lab_server.py --port 8103

Bugs, on purpose.

- Object authorization checks the token but not the owner.
- The user update binds the role field.
- The GraphQL endpoint runs every alias under one request.
- The export endpoint fetches any URL.

"""

from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

USERS = {
    1: {"id": 1, "name": "alice", "role": "user", "email": "alice@lab.local"},
    2: {"id": 2, "name": "bob", "role": "user", "email": "bob@lab.local"},
    3: {"id": 3, "name": "admin", "role": "admin", "email": "admin@lab.local"},
}
TOKENS = {"alice-token": 1, "bob-token": 2}
ALIAS_RE = re.compile(r"(\w+)\s*:\s*user\s*\(\s*id\s*:\s*(\d+)\s*\)")
USER_RE = re.compile(r"user\s*\(\s*id\s*:\s*(\d+)\s*\)")

INDEX = """<h1>API lab</h1>
<p>Use Authorization: Bearer alice-token or bob-token.</p>
<a href="/api/users/1">user 1</a><br>
<a href="/graphql?query={user(id:1){name}}">graphql</a><br>
<a href="/api/export?url=http://127.0.0.1:8103/health">export</a><br>
<a href="/health">health</a>"""


class Handler(BaseHTTPRequestHandler):
    server_version = "ApiLab/0.1"

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"{self.address_string()} - " + (fmt % args))

    def send(self, body: str, code: int = 200, ctype: str = "application/json") -> None:
        raw = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def uid(self) -> int:
        token = self.headers.get("Authorization", "").removeprefix("Bearer ").strip()
        return TOKENS.get(token, 0)

    def do_GET(self) -> None:
        parts = urllib.parse.urlsplit(self.path)
        path, q = parts.path, urllib.parse.parse_qs(parts.query)
        if path == "/":
            return self.send(INDEX, ctype="text/html")
        if path == "/health":
            return self.send("ok", ctype="text/plain")
        if path.startswith("/api/users/"):
            if not self.uid():
                return self.send(json.dumps({"error": "auth"}), 401)
            try:
                uid = int(path.rsplit("/", 1)[-1])
            except ValueError:
                return self.send(json.dumps({"error": "bad id"}), 400)
            user = USERS.get(uid)
            return self.send(json.dumps(user) if user else json.dumps({"error": "not found"}), 200 if user else 404)
        if path == "/graphql":
            query = q.get("query", [""])[0] or self.headers.get("X-Query", "")
            aliases = ALIAS_RE.findall(query)
            if aliases:
                data = {alias: USERS.get(int(uid)) for alias, uid in aliases}
                return self.send(json.dumps({"data": data}))
            match = USER_RE.search(query)
            if match:
                user = USERS.get(int(match.group(1)))
                return self.send(json.dumps({"data": {"user": user}}))
            return self.send(json.dumps({"errors": ["unsupported query"]}), 400)
        if path == "/api/export":
            url = q.get("url", [""])[0]
            try:
                body = urllib.request.urlopen(url, timeout=3).read(4000).decode("utf-8", "replace")
                return self.send(json.dumps({"url": url, "body": body}))
            except Exception as exc:
                return self.send(json.dumps({"url": url, "error": str(exc)}), 502)
        return self.send(json.dumps({"error": "not found"}), 404)

    def do_PATCH(self) -> None:
        parts = urllib.parse.urlsplit(self.path)
        if not parts.path.startswith("/api/users/"):
            return self.send(json.dumps({"error": "not found"}), 404)
        if not self.uid():
            return self.send(json.dumps({"error": "auth"}), 401)
        try:
            uid = int(parts.path.rsplit("/", 1)[-1])
        except ValueError:
            return self.send(json.dumps({"error": "bad id"}), 400)
        user = USERS.get(uid)
        if not user:
            return self.send(json.dumps({"error": "not found"}), 404)
        length = int(self.headers.get("Content-Length", "0"))
        try:
            body = json.loads(self.rfile.read(min(length, 100_000)) or b"{}")
        except json.JSONDecodeError:
            return self.send(json.dumps({"error": "bad json"}), 400)
        for key in ("name", "email", "role"):
            if key in body:
                user[key] = body[key]
        return self.send(json.dumps(user))


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8103)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"lab on http://{args.host}:{args.port}")
    srv.serve_forever()


if __name__ == "__main__":
    main()
