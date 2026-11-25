#!/usr/bin/env bash
# Smoke tests for the API lab.
set -uo pipefail
PORT="${PORT:-$(python3 -c 'import socket;s=socket.socket();s.bind(("127.0.0.1",0));print(s.getsockname()[1]);s.close()')}"
BASE="http://127.0.0.1:$PORT"
DIR="$(cd "$(dirname "$0")" && pwd)"
PASS=0
FAIL=0

python3 "$DIR/lab_server.py" --port "$PORT" >/tmp/beril-api-lab.log 2>&1 &
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

check "bola" "admin@lab.local" "$(curl -s -H 'Authorization: Bearer bob-token' "$BASE/api/users/3")"
check "mass assignment" '"role": "admin"' "$(curl -s -X PATCH -H 'Authorization: Bearer bob-token' -H 'Content-Type: application/json' --data '{"role":"admin"}' "$BASE/api/users/2")"
QUERY='{a:user(id:1){name} b:user(id:2){name} c:user(id:3){name}}'
check "graphql alias batch" "admin" "$(curl -s --get --data-urlencode "query=$QUERY" "$BASE/graphql")"
check "ssrf" "ok" "$(curl -s --get --data-urlencode "url=$BASE/health" "$BASE/api/export")"
check "auth required" "auth" "$(curl -s "$BASE/api/users/1")"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
