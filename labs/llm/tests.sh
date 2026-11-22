#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"
PASS=0
FAIL=0
ok() { echo "PASS $1"; PASS=$((PASS+1)); }
no() { echo "FAIL $1"; FAIL=$((FAIL+1)); }

grep -q 'sk_live_' app_spec.md && ok "key in spec" || no "key in spec"
grep -q 'send_email' app_spec.md && ok "send tool" || no "send tool"
grep -qi 'no tenant filter' app_spec.md && ok "tenant gap documented" || no "tenant gap documented"
grep -q 'billing@evil.lab' transcripts/02_indirect.md && ok "indirect injection" || no "indirect injection"
grep -q 'evil.lab/p?d=' transcripts/03_exfil.md && ok "markdown exfil" || no "markdown exfil"
grep -q 'users/77' transcripts/04_cross_user.md && ok "cross-user leak" || no "cross-user leak"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
