#!/usr/bin/env bash
# Ghidra headless wrapper for one binary.
#   GHIDRA_HOME=~/tools/ghidra ./scripts/ghidra_headless.sh ./sample out.json
set -euo pipefail

BIN="${1:?usage: ghidra_headless.sh <binary> [out.json]}"
OUT="${2:-scans/$(basename "$BIN").ghidra.json}"
HOME_GHIDRA="${GHIDRA_HOME:-$HOME/tools/ghidra}"
ANALYZE="$HOME_GHIDRA/support/analyzeHeadless"

if [ ! -x "$ANALYZE" ]; then
  echo "analyzeHeadless not found. Set GHIDRA_HOME to the Ghidra install directory." >&2
  exit 1
fi
mkdir -p "$(dirname "$OUT")" "$(dirname "$OUT")/ghidra-project"
PROJECT="$(mktemp -d "${TMPDIR:-/tmp}/beril-ghidra-XXXX")"
trap 'rm -rf "$PROJECT"' EXIT

BERIL_GHIDRA_OUT="$(realpath "$OUT")" "$ANALYZE" "$PROJECT" beril \
  -import "$(realpath "$BIN")" -overwrite \
  -postScript ghidra_dump.py -scriptPath "$(dirname "$0")" \
  -deleteProject

echo "wrote $OUT"
