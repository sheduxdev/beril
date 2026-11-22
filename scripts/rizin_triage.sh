#!/usr/bin/env bash
# JSON triage with rizin. Requires rizin or radare2.
set -euo pipefail
BIN="${1:?usage: rizin_triage.sh <binary> [out.json]}"
OUT="${2:-scans/$(basename "$BIN").rizin.json}"
TOOL="$(command -v rizin || command -v radare2 || true)"
[ -n "$TOOL" ] || { echo "rizin or radare2 required" >&2; exit 1; }
mkdir -p "$(dirname "$OUT")"
"$TOOL" -q -j -c 'iI;iS;iE;ii;iz;afl' "$BIN" > "$OUT"
echo "wrote $OUT"
