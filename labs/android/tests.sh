#!/usr/bin/env bash
# Smoke tests for the Android lab artifacts.
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

check "exported webview" 'WebViewActivity" android:exported="true"' "AndroidManifest.xml"
check "debuggable" 'android:debuggable="true"' "AndroidManifest.xml"
check "backup on" 'android:allowBackup="true"' "AndroidManifest.xml"
check "cleartext" 'usesCleartextTraffic="true"' "AndroidManifest.xml"
check "unverified deep link" 'autoVerify="false"' "AndroidManifest.xml"
check "root provider path" 'root-path' "file_paths.xml"
check "token" "android-lab-3d9e" "strings.txt"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
