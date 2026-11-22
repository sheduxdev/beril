#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"
PY="$(cd ../.. && pwd)/.venv/bin/python"
[ -x "$PY" ] || PY=python3
OUT=$("$PY" matcher.py --log access.log --rule rules/cgi_injection.yml)
echo "$OUT"
grep -q 'hits=3' <<<"$OUT" && echo "PASS three hits" || echo "FAIL three hits"
grep -q 'index.html' <<<"$OUT" && echo "FAIL false positive" || echo "PASS no index hit"
grep -q 't1059.004' rules/cgi_injection.yml && echo "PASS ATT&CK tag" || echo "FAIL ATT&CK tag"
