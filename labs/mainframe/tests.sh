#!/usr/bin/env bash
# Smoke tests for the mainframe lab artifacts.
set -uo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
PASS=0
FAIL=0

check() {
  local name="$1" needle="$2" file="$3"
  if grep -q "$needle" "$DIR/$file"; then
    echo "PASS $name"; PASS=$((PASS+1))
  else
    echo "FAIL $name"; FAIL=$((FAIL+1))
  fi
}

check "special user" "SVCBACK" "racf-profiles.txt"
check "alter grant" "PROD.BACKUP.**" "racf-profiles.txt"
check "apf writable" "PROD.APF.LOAD     VOL=PRD01  WRITE=YES" "apf.txt"
check "ceci" "CECI" "cics-transactions.txt"
check "cedf" "CEDF" "cics-transactions.txt"
check "start denied" "NOT AUTHORIZED" "console.txt"
check "jcl write" "PROD.BACKUP.NEW" "jcl/backup.jcl"
check "db2 all" "GRANT ALL ON PROD.BACKUP_LOG" "db2-grants.txt"
check "spool leak" "PAYROLL RUN" "jes-spool.txt"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
