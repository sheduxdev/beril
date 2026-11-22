#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"
PASS=0
FAIL=0
ok() { echo "PASS $1"; PASS=$((PASS+1)); }
no() { echo "FAIL $1"; FAIL=$((FAIL+1)); }

grep -q 'public-read' main.tf && ok "public bucket" || no "public bucket"
grep -q '0.0.0.0/0' main.tf && ok "world-open port" || no "world-open port"
grep -q 'publicly_accessible  = true' main.tf && ok "public database" || no "public database"
grep -q 'Action   = "\*"' main.tf && ok "wildcard IAM" || no "wildcard IAM"
grep -q 'privileged: true' debug-pod.yaml && ok "privileged pod" || no "privileged pod"
grep -q 'runAsUser: 0' debug-pod.yaml && ok "root pod" || no "root pod"
grep -q 'FROM node:latest' Dockerfile && ok "unpinned base" || no "unpinned base"
grep -q 'API_KEY=' Dockerfile && ok "build-time key" || no "build-time key"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
