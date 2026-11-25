#!/usr/bin/env python3
"""Deliberately broken auth lab. Standard library only, local only.

    python labs/auth/lab_server.py --port 8101

Bugs, on purpose.

- The session id does not rotate at login.
- MFA is a flag the API ignores.
- The reset token is a counter and it is reusable.
- The admin JWT accepts alg none.

"""

from __future__ import annotations

import base64
import json
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

USERS = {"alice": "alice-pass", "admin": "admin-pass"}
SESSIONS: dict[str, dict] = {}
RESET = {"alice": "1001", "admin": "1002"}
COUNTER = 1000

INDEX = """<h1>Auth lab</h1>
<a href="/login?user=alice">login alice</a><br>
<a href="/session">session</a><br>
<a href="/mfa/login?user=alice">mfa login step</a><br>
<a href="/mfa/verify?otp=123456">mfa verify</a><br>
<a href="/api/profile">api profile</a><br>
<a href="/reset?user=alice">reset token</a><br>
<a href="/token?user=alice">sample jwt</a><br>
<a href="/admin">admin</a><br>
<a href="/health">health</a>"""


def b64(data: dict) -> str:
    raw = json.dumps(data, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def unb64(part: str) -> dict:
    pad = "=" * (-len(part) % 4)
    return json.loads(base64.urlsafe_b64decode(part + pad))


class Handler(BaseHTTPRequestHandler):
    server_version = "AuthLab/0.1"

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"{self.address_string()} - " + (fmt % args))

    def send(
        self, body: str, code: int = 200, ctype: str = "text/html; charset=utf-8", headers: dict | None = None
    ) -> None:
        raw = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(raw)

    def sid(self) -> str:
        for part in self.headers.get("Cookie", "").split(";"):
            key, _, value = part.strip().partition("=")
            if key == "sid":
                return value
        return ""

    def do_GET(self) -> None:
        global COUNTER
        parts = urllib.parse.urlsplit(self.path)
        path, q = parts.path, urllib.parse.parse_qs(parts.query)
        if path == "/":
            return self.send(INDEX)
        if path == "/health":
            return self.send("ok", ctype="text/plain")
        if path == "/login":
            user = q.get("user", ["alice"])[0]
            if user not in USERS:
                return self.send("no user", 404)
            sid = self.sid() or f"fixed-{user}"
            SESSIONS[sid] = {"user": user, "mfa": False}
            return self.send(f"hello {user}", headers={"Set-Cookie": f"sid={sid}; Path=/; HttpOnly"})
        if path == "/session":
            session = SESSIONS.get(self.sid())
            if not session:
                return self.send("anonymous")
            return self.send(f"user={session['user']} mfa={session['mfa']} sid={self.sid()}")
        if path == "/mfa/login":
            user = q.get("user", ["alice"])[0]
            sid = self.sid() or f"fixed-{user}"
            SESSIONS[sid] = {"user": user, "mfa": False}
            return self.send("password ok, send otp", headers={"Set-Cookie": f"sid={sid}; Path=/"})
        if path == "/mfa/verify":
            if q.get("otp", [""])[0] != "123456":
                return self.send("bad otp", 401)
            session = SESSIONS.get(self.sid())
            if not session:
                return self.send("no session", 401)
            session["mfa"] = True
            return self.send("mfa ok")
        if path == "/api/profile":
            session = SESSIONS.get(self.sid())
            if not session:
                return self.send('{"error":"auth"}', 401, "application/json")
            return self.send(
                json.dumps({"user": session["user"], "role": "user", "mfa": session["mfa"]}), ctype="application/json"
            )
        if path == "/reset":
            user = q.get("user", ["alice"])[0]
            COUNTER += 1
            token = str(COUNTER)
            RESET[user] = token
            return self.send(f"reset token for {user} is {token}")
        if path == "/reset/confirm":
            user = q.get("user", ["alice"])[0]
            token = q.get("token", [""])[0]
            new = q.get("password", [""])[0]
            if RESET.get(user) != token:
                return self.send("bad token", 400)
            USERS[user] = new
            return self.send("password changed, token still valid")
        if path == "/token":
            user = q.get("user", ["alice"])[0]
            header = b64({"alg": "none", "typ": "JWT"})
            payload = b64({"sub": user, "role": "admin" if user == "admin" else "user"})
            return self.send(f"{header}.{payload}.", ctype="text/plain")
        if path == "/admin":
            raw = self.headers.get("Authorization", "").removeprefix("Bearer ").strip()
            parts = raw.split(".")
            if len(parts) != 3:
                return self.send("missing token", 401)
            try:
                header = unb64(parts[0])
                payload = unb64(parts[1])
            except Exception:
                return self.send("bad token", 400)
            if header.get("alg") != "none":
                return self.send("only alg none is accepted here", 401)
            if payload.get("role") != "admin":
                return self.send("not admin", 403)
            return self.send("<h1>Admin</h1><p>flag AUTH-JWT-NONE</p>")
        return self.send("not found", 404)


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8101)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"lab on http://{args.host}:{args.port}")
    srv.serve_forever()


if __name__ == "__main__":
    main()
