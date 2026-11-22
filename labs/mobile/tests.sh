#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"
M=app/src/main/AndroidManifest.xml
PASS=0
FAIL=0
ok() { echo "PASS $1"; PASS=$((PASS+1)); }
no() { echo "FAIL $1"; FAIL=$((FAIL+1)); }

grep -q 'DebugActivity" android:exported="true"' "$M" && ok "debug activity exported" || no "debug activity exported"
grep -q 'TokenReceiver" android:exported="true"' "$M" && ok "receiver exported" || no "receiver exported"
grep -q 'android:scheme="beril"' "$M" && ok "deep link present" || no "deep link present"
grep -q 'allowBackup="true"' "$M" && ok "backup enabled" || no "backup enabled"
grep -q 'cleartextTrafficPermitted="true"' app/src/main/res/xml/network_security_config.xml && ok "cleartext allowed" || no "cleartext allowed"
grep -q 'addJavascriptInterface' app/src/main/java/com/beril/lab/MainActivity.java && ok "js bridge" || no "js bridge"
grep -q 'AIza' app/src/main/res/values/strings.xml && ok "embedded key" || no "embedded key"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
