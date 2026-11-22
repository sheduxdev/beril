#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"
python3 build_firmware.py >/dev/null
rm -rf out
../../.venv/bin/unblob firmware.bin -e out >/tmp/beril-fw.log 2>&1 || true
ROOT=$(find out -type d -name '*.zip_extract' | head -1)
PASS=0
FAIL=0
ok() { echo "PASS $1"; PASS=$((PASS+1)); }
no() { echo "FAIL $1"; FAIL=$((FAIL+1)); }

[ -n "$ROOT" ] && ok "firmware extracted" || no "firmware extracted"
[ -f "$ROOT/etc/passwd" ] && ok "passwd found" || no "passwd found"
[ -f "$ROOT/etc/update.conf" ] && grep -q 'VERIFY=0' "$ROOT/etc/update.conf" && ok "update verification off" || no "update verification off"
[ -f "$ROOT/etc/app.env" ] && grep -q 'AKIA' "$ROOT/etc/app.env" && ok "key in env file" || no "key in env file"
[ -f "$ROOT/etc/init.d/rcS" ] && grep -q 'telnetd' "$ROOT/etc/init.d/rcS" && ok "telnet service" || no "telnet service"

if [ -n "$ROOT" ]; then
  OUT=$(QUERY_STRING='host=127.0.0.1; id' sh "$ROOT/www/cgi-bin/diagnostic.cgi" 2>&1)
  grep -q 'uid=' <<<"$OUT" && ok "cgi command injection" || no "cgi command injection"
else
  no "cgi command injection"
fi

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
