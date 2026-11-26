#!/usr/bin/env bash
# Smoke tests for the macOS lab artifacts.
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

check "ats arbitrary" "NSAllowsArbitraryLoads" "Sample.app/Contents/Info.plist"
check "library validation off" "disable-library-validation" "Sample.app/Contents/entitlements.plist"
check "jit allowed" "allow-jit" "Sample.app/Contents/entitlements.plist"
check "launchd writable path" "/Users/Shared/agent/run.sh" "launchd/com.example.agent.plist"
check "adhoc signature" "adhoc" "codesign.txt"
check "full disk access" "SystemPolicyAllFiles" "tcc.txt"
check "token in bundle" "APNS_TOKEN" "Sample.app/Contents/config.env"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
