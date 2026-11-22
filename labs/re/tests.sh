#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"
make -s clean all
OUT=$(./challenge 'BERLosoy0751')
echo "good: $OUT"
grep -q 'flag{' <<<"$OUT" && echo "PASS valid input" || echo "FAIL valid input"
./challenge WRONG >/dev/null 2>&1
[ $? -ne 0 ] && echo "PASS wrong input" || echo "FAIL wrong input"
file challenge | grep -q 'stripped' && echo "PASS binary stripped" || echo "note: binary not stripped"
