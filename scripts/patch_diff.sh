#!/usr/bin/env bash
# Patch-diff helper. Modes: ghidriff, bindiff, diaphora, git.
#   ./scripts/patch_diff.sh ghidriff old.bin new.bin
#   ./scripts/patch_diff.sh bindiff old.i64 new.i64
#   ./scripts/patch_diff.sh git ./repo v1.2.3 v1.2.4
set -euo pipefail
MODE="${1:?usage: patch_diff.sh <ghidriff|bindiff|diaphora|git> <old> <new> [args]}"
OLD="${2:?old artifact required}"
NEW="${3:?new artifact required}"

case "$MODE" in
  ghidriff)
    command -v ghidriff >/dev/null || { echo "ghidriff required: pip install ghidriff" >&2; exit 1; }
    ghidriff "$OLD" "$NEW" -o "scans/diff-$(basename "$OLD")-$(basename "$NEW")"
    ;;
  bindiff)
    command -v bindiff >/dev/null || { echo "BinDiff required (IDA plugin or CLI)" >&2; exit 1; }
    bindiff --primary "$OLD" --secondary "$NEW" --output "scans/diff.BinDiff"
    ;;
  diaphora)
    echo "Open the old database in IDA, run Diaphora, choose the new database as secondary."
    echo "CLI: python3 diaphora.py -h"
    ;;
  git)
    cd "$OLD"
    git log --oneline "$NEW..$OLD" 2>/dev/null || true
    git diff "$NEW" "$OLD" --stat
    echo "Review the changed files, then the changed functions."
    ;;
  *)
    echo "unknown mode: $MODE" >&2
    exit 1
    ;;
esac
