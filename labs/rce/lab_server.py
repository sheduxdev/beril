#!/usr/bin/env python3
"""Deliberately vulnerable RCE lab. Standard library only, local only.

    python labs/rce/lab_server.py --port 8100

Bugs, on purpose.

- /cmd and /blind pass the host to a shell.
- /calc evaluates the expression with eval.
- /deser unpickles a base64 blob.
- /upload writes a file and /plugin executes it.

Never expose this server to the internet.
"""

from __future__ import annotations

import base64
import contextlib
import io
import os
import pickle
import subprocess
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOADS = os.path.join(ROOT, "uploads")
LOG = os.path.join(ROOT, "access.log")

INDEX = """<h1>RCE lab</h1>
<p>Every endpoint is deliberately broken.</p>
<a href="/cmd?host=127.0.0.1">cmd, visible output</a><br>
<a href="/blind?host=127.0.0.1">blind, timing or file proof</a><br>
<a href="/calc?expr=6*7">calc, eval</a><br>
<a href="/read?file=secret.env">read, path traversal</a><br>
<a href="/deser?data=">deser, base64 pickle</a><br>
<form action="/upload?name=plugin.py" method="post" enctype="text/plain">
  <textarea name="code" rows="4" cols="50">print(__import__("os").popen("id").read())</textarea>
  <button>upload</button>
</form>
<a href="/plugin?name=plugin.py">plugin, execute the upload</a><br>
<a href="/health">health</a>"""


class Handler(BaseHTTPRequestHandler):
    server_version = "RceLab/0.1"

    def log_message(self, fmt: str, *args: object) -> None:
        line = f"{self.address_string()} - " + (fmt % args) + "\n"
        print(line, end="")
        with open(LOG, "a", encoding="utf-8") as fh:
            fh.write(line)

    def send(self, body: str | bytes, code: int = 200, ctype: str = "text/html; charset=utf-8") -> None:
        raw = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def shell(self, host: str) -> tuple[str, int]:
        try:
            proc = subprocess.run(
                f"getent hosts {host}",
                shell=True,
                capture_output=True,
                text=True,
                timeout=5,
            )
            return (proc.stdout or "") + (proc.stderr or ""), proc.returncode
        except subprocess.TimeoutExpired:
            return "timeout", 124

    def do_GET(self) -> None:
        parts = urllib.parse.urlsplit(self.path)
        path, q = parts.path, urllib.parse.parse_qs(parts.query)
        if path == "/":
            return self.send(INDEX)
        if path == "/health":
            return self.send("ok", ctype="text/plain")
        if path == "/cmd":
            out, code = self.shell(q.get("host", ["127.0.0.1"])[0])
            return self.send(f"<h1>Result</h1><pre>{out}</pre><p>exit {code}</p>")
        if path == "/blind":
            self.shell(q.get("host", ["127.0.0.1"])[0])
            return self.send("<h1>Checked</h1><p>Output is not returned.</p>")
        if path == "/calc":
            expr = q.get("expr", ["6*7"])[0]
            try:
                value = eval(expr, {"__builtins__": __builtins__}, {})
                return self.send(f"<h1>Calc</h1><p>{value!r}</p>")
            except Exception as exc:
                return self.send(f"<h1>Calc error</h1><p>{type(exc).__name__}: {exc}</p>", 500)
        if path == "/deser":
            try:
                blob = base64.b64decode(q.get("data", [""])[0])
            except Exception as exc:
                return self.send(f"bad base64: {exc}", 400)
            try:
                value = pickle.loads(blob)
            except Exception as exc:
                return self.send(f"pickle error: {type(exc).__name__}: {exc}", 500)
            return self.send(f"<h1>Object</h1><pre>{value!r}</pre>")
        if path == "/read":
            name = q.get("file", ["notes.txt"])[0]
            full = os.path.join(ROOT, name)
            try:
                with open(full, encoding="utf-8", errors="replace") as fh:
                    return self.send(fh.read(), ctype="text/plain")
            except OSError as exc:
                return self.send(f"cannot read {full}: {exc}", 404)
        if path == "/plugin":
            name = os.path.basename(q.get("name", ["plugin.py"])[0])
            full = os.path.join(UPLOADS, name)
            try:
                with open(full, encoding="utf-8", errors="replace") as fh:
                    code = fh.read()
            except OSError as exc:
                return self.send(f"cannot load {full}: {exc}", 404)
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                    exec(compile(code, name, "exec"), {"__name__": "__lab__"})
            except Exception as exc:
                return self.send(f"<h1>Plugin error</h1><pre>{buf.getvalue()}{type(exc).__name__}: {exc}</pre>", 500)
            return self.send(f"<h1>Plugin output</h1><pre>{buf.getvalue()}</pre>")
        return self.send("not found", 404)

    def do_POST(self) -> None:
        parts = urllib.parse.urlsplit(self.path)
        q = urllib.parse.parse_qs(parts.query)
        if parts.path != "/upload":
            return self.send("not found", 404)
        name = os.path.basename(q.get("name", ["file.bin"])[0]) or "file.bin"
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(min(length, 1_000_000))
        if body.startswith(b"code="):
            body = urllib.parse.unquote_plus(body[5:].decode("utf-8", "replace")).encode("utf-8")
        os.makedirs(UPLOADS, exist_ok=True)
        full = os.path.join(UPLOADS, name)
        with open(full, "wb") as fh:
            fh.write(body)
        return self.send(f"<h1>Stored</h1><p>{full}</p><a href='/plugin?name={urllib.parse.quote(name)}'>execute</a>")


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8100)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    os.makedirs(UPLOADS, exist_ok=True)
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"lab on http://{args.host}:{args.port}")
    srv.serve_forever()


if __name__ == "__main__":
    main()
