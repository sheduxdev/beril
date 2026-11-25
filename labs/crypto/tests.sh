#!/usr/bin/env bash
# Smoke tests for the crypto lab.
set -uo pipefail
PORT="${PORT:-$(python3 -c 'import socket;s=socket.socket();s.bind(("127.0.0.1",0));print(s.getsockname()[1]);s.close()')}"
BASE="http://127.0.0.1:$PORT"
DIR="$(cd "$(dirname "$0")" && pwd)"
PASS=0
FAIL=0

python3 "$DIR/lab_server.py" --port "$PORT" >/tmp/beril-crypto-lab.log 2>&1 &
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

ECB=$(curl -s --get --data-urlencode 'data=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' "$BASE/ecb")
B1=${ECB:0:32}
B2=${ECB:32:32}
check "ecb equal blocks" "$B1" "$B2"

CBC=$(curl -s --get --data-urlencode 'data=AAAAAAAAAAAAAAAA' "$BASE/cbc")
IV=${CBC%%:*}
CT=${CBC##*:}
check "padding valid" "valid" "$(curl -s --get --data-urlencode "data=$IV$CT" "$BASE/padding")"
LAST=${CT: -2}
if [ "$LAST" = "00" ]; then NEW="01"; else NEW=$(printf '%02x' $((16#$LAST ^ 1))); fi
BAD="$IV${CT:0:${#CT}-2}$NEW"
check "padding invalid" "invalid" "$(curl -s --get --data-urlencode "data=$BAD" "$BASE/padding")"

NONCE="0102030405060708090a0b0c0d0e0f10"
A=$(curl -s --get --data-urlencode 'data=AAAAAAAAAAAAAAAA' --data-urlencode "nonce=$NONCE" "$BASE/stream")
B=$(curl -s --get --data-urlencode 'data=BBBBBBBBBBBBBBBB' --data-urlencode "nonce=$NONCE" "$BASE/stream")
X=$(python3 - "$A" "$B" <<'PY'
import sys
a=bytes.fromhex(sys.argv[1]); b=bytes.fromhex(sys.argv[2])
print((bytes(x^y for x,y in zip(a,b))).hex())
PY
)
check "stream nonce reuse" "030303" "$X"

H1=$(curl -s --get --data-urlencode 'data=hello' "$BASE/hash")
H2=$(curl -s --get --data-urlencode 'data=hello' "$BASE/hash")
check "md5 deterministic" "$H1" "$H2"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
