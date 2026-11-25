#!/usr/bin/env bash
# Smoke tests for the auth lab.
set -uo pipefail
PORT="${PORT:-$(python3 -c 'import socket;s=socket.socket();s.bind(("127.0.0.1",0));print(s.getsockname()[1]);s.close()')}"
BASE="http://127.0.0.1:$PORT"
DIR="$(cd "$(dirname "$0")" && pwd)"
PASS=0
FAIL=0

python3 "$DIR/lab_server.py" --port "$PORT" >/tmp/beril-auth-lab.log 2>&1 &
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

COOKIE=$(mktemp)
curl -s -c "$COOKIE" "$BASE/login?user=alice" >/dev/null
check "session fixation" "fixed-alice" "$(curl -s -b "$COOKIE" "$BASE/session")"
check "mfa skip" '"mfa": false' "$(curl -s -b "$COOKIE" "$BASE/api/profile")"
TOKEN=$(curl -s --get --data-urlencode 'user=alice' "$BASE/reset" | awk '{print $NF}')
check "reset reuse" "changed" "$(curl -s --get --data-urlencode 'user=alice' --data-urlencode "token=$TOKEN" --data-urlencode 'password=new-pass' "$BASE/reset/confirm")"
check "reset token weak" "100" "$TOKEN"

JWT=$(curl -s --get --data-urlencode 'user=alice' "$BASE/token")
HEADER=$(cut -d. -f1 <<<"$JWT")
PAYLOAD=$(printf '{"sub":"alice","role":"admin"}' | base64 | tr '+/' '-_' | tr -d '=\n')
FORGED="$HEADER.$PAYLOAD."
check "jwt none" "AUTH-JWT-NONE" "$(curl -s -H "Authorization: Bearer $FORGED" "$BASE/admin")"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
