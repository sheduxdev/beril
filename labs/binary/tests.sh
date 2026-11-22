#!/usr/bin/env bash
# Smoke tests for the binary lab.
set -uo pipefail
cd "$(dirname "$0")"
make -s clean all integer-asan || exit 1
PASS=0
FAIL=0

ok() { echo "PASS $1"; PASS=$((PASS+1)); }
no() { echo "FAIL $1"; FAIL=$((FAIL+1)); }

python3 -c 'print("A"*120)' | ./stack-vuln >/dev/null 2>&1
[ $? -eq 139 ] && ok "stack overflow crashes" || no "stack overflow crashes"

readelf -h stack-vuln | grep -q 'EXEC' && ok "vuln build is non-PIE" || no "vuln build is non-PIE"
readelf -h stack-hard | grep -q 'DYN' && ok "hard build is PIE" || no "hard build is PIE"

printf '%%p.%%p.%%p\n' | ./fmt | grep -q '0x' && ok "format string leaks" || no "format string leaks"

ADDR=$(nm uaf | awk '/ win$/{print $1}')
python3 -c "import sys,struct;sys.stdout.buffer.write(struct.pack('<Q',0x$ADDR)+b'B'*24)" | ./uaf | grep -q 'flag{' && ok "uaf calls win" || no "uaf calls win"

OUT=$(python3 -c 'print("A"*2000)' | ./integer-asan 65536 65536 2>&1)
grep -q 'AddressSanitizer' <<<"$OUT" && ok "integer wrap is caught by ASAN" || no "integer wrap is caught by ASAN"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
