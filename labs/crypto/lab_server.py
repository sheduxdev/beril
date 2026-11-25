#!/usr/bin/env python3
"""Deliberately broken crypto lab. Openssl CLI, local only.

    python labs/crypto/lab_server.py --port 8102

Bugs, on purpose.

- ECB mode on controlled input.
- CBC decryption that reports padding validity.
- CTR with a caller chosen nonce.
- MD5(secret + message) as a MAC.

"""

from __future__ import annotations

import binascii
import hashlib
import subprocess
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

KEY = "00112233445566778899aabbccddeeff"
IV = "0102030405060708090a0b0c0d0e0f10"
SECRET = b"s3cr3t"

INDEX = """<h1>Crypto lab</h1>
<a href="/ecb?data=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA">ecb, 32 A</a><br>
<a href="/cbc?data=hello">cbc, encrypted</a><br>
<a href="/padding?data=">padding oracle, hex input</a><br>
<a href="/stream?data=AAAAAAAAAAAAAAAA&nonce=0102030405060708090a0b0c0d0e0f10">stream, fixed nonce</a><br>
<a href="/hash?data=hello">md5(secret + data)</a><br>
<a href="/health">health</a>"""


def openssl(args: list[str], data: bytes) -> bytes:
    proc = subprocess.run(["openssl", "enc", *args], input=data, capture_output=True)
    if proc.returncode != 0:
        raise ValueError(proc.stderr.decode("utf-8", "replace"))
    return proc.stdout


def pkcs7_ok(data: bytes) -> bool:
    if not data or len(data) % 16:
        return False
    pad = data[-1]
    if pad < 1 or pad > 16 or pad > len(data):
        return False
    return data[-pad:] == bytes([pad]) * pad


class Handler(BaseHTTPRequestHandler):
    server_version = "CryptoLab/0.1"

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"{self.address_string()} - " + (fmt % args))

    def send(self, body: str, code: int = 200, ctype: str = "text/html; charset=utf-8") -> None:
        raw = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:
        parts = urllib.parse.urlsplit(self.path)
        path, q = parts.path, urllib.parse.parse_qs(parts.query)
        data = q.get("data", [""])[0]
        if path == "/":
            return self.send(INDEX)
        if path == "/health":
            return self.send("ok", ctype="text/plain")
        if path == "/ecb":
            try:
                out = openssl(["-aes-128-ecb", "-K", KEY], data.encode())
            except ValueError as exc:
                return self.send(f"error: {exc}", 500)
            return self.send(binascii.hexlify(out).decode(), ctype="text/plain")
        if path == "/cbc":
            try:
                out = openssl(["-aes-128-cbc", "-K", KEY, "-iv", IV], data.encode())
            except ValueError as exc:
                return self.send(f"error: {exc}", 500)
            return self.send(IV + ":" + binascii.hexlify(out).decode(), ctype="text/plain")
        if path == "/padding":
            try:
                blob = binascii.unhexlify(data)
                out = openssl(["-aes-128-cbc", "-d", "-K", KEY, "-iv", IV, "-nopad"], blob)
            except (ValueError, binascii.Error):
                return self.send("invalid", 400)
            return self.send("valid" if pkcs7_ok(out) else "invalid", 400 if not pkcs7_ok(out) else 200, "text/plain")
        if path == "/stream":
            nonce = q.get("nonce", [IV])[0]
            try:
                out = openssl(["-aes-128-ctr", "-K", KEY, "-iv", nonce], data.encode())
            except ValueError as exc:
                return self.send(f"error: {exc}", 500)
            return self.send(binascii.hexlify(out).decode(), ctype="text/plain")
        if path == "/hash":
            return self.send(hashlib.md5(SECRET + data.encode()).hexdigest(), ctype="text/plain")
        return self.send("not found", 404)


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8102)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"lab on http://{args.host}:{args.port}")
    srv.serve_forever()


if __name__ == "__main__":
    main()
