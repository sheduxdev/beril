#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"
PASS=0
FAIL=0
ok() { echo "PASS $1"; PASS=$((PASS+1)); }
no() { echo "FAIL $1"; FAIL=$((FAIL+1)); }

grep -q 'MSSQLSvc/backup.lab' users.json && ok "roastable SPN" || no "roastable SPN"
grep -q 'Helpdesk,svc_sql,GenericAll' acls.csv && ok "ACL edge" || no "ACL edge"
grep -q 'svc_sql,APP01,AdminTo' acls.csv && ok "local admin edge" || no "local admin edge"
grep -q 'WebServer,Helpdesk,false,true,true' adcs.csv && ok "ESC1 template" || no "ESC1 template"
grep -q 'Backup Operators' users.json && ok "backup group" || no "backup group"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
