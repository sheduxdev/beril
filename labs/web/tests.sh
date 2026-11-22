#!/usr/bin/env bash
# Smoke tests for the web lab. Prints PASS or FAIL for each expected bug.
set -uo pipefail
PORT="${PORT:-$(python3 -c 'import socket;s=socket.socket();s.bind(("127.0.0.1",0));print(s.getsockname()[1]);s.close()')}"
BASE="http://127.0.0.1:$PORT"
DIR="$(cd "$(dirname "$0")" && pwd)"
PASS=0
FAIL=0

python3 "$DIR/lab_server.py" --port "$PORT" >/tmp/beril-web-lab.log 2>&1 &
PID=$!
trap 'kill $PID 2>/dev/null' EXIT
sleep 1

check() {
  local name="$1" needle="$2" haystack="$3"
  if grep -q "$needle" <<<"$haystack"; then
    echo "PASS $name"; PASS=$((PASS+1))
  else
    echo "FAIL $name"; FAIL=$((FAIL+1))
  fi
}

check "index" "Beril lab" "$(curl -s "$BASE/")"
check "idor profile" "bob@lab.local" "$(curl -s "$BASE/profile?id=2")"
check "reflected xss" "<script>alert(1)</script>" "$(curl -s --get --data-urlencode 'q=<script>alert(1)</script>' "$BASE/search")"
check "sqli" "pistachio" "$(curl -s --get --data-urlencode 'id=1 OR 1=1' "$BASE/item")"
check "traversal" "beril" "$(curl -s --get --data-urlencode 'file=../../README.md' "$BASE/download")"
check "ssrf" "ok" "$(curl -s --get --data-urlencode "url=$BASE/health" "$BASE/fetch")"
check "client role" "PISTACHIO-ADMIN-42" "$(curl -s -b 'role=admin' "$BASE/admin")"
check "api leak" "bob@lab.local" "$(curl -s "$BASE/api/users/2")"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
