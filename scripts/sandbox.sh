#!/usr/bin/env bash
# Sandboxed build and test for the bug hunt line.
#
# Network is off, the source mount is read-only, the work copy is tmpfs, all
# capabilities are dropped and the process runs as a non-root user. It still
# is not a hypervisor: do not point it at a hostile binary you have not looked
# at, and keep Docker updated.
#
#   ./scripts/sandbox.sh --target ./repo --lang python
#   ./scripts/sandbox.sh --target ./repo --lang c --run "./a.out"
#   ./scripts/sandbox.sh --target ./repo --lang go --dry-run
set -uo pipefail

TARGET=""
LANG=""
BUILD=""
RUN=""
TIMEOUT=300
DRY=0

usage() {
  sed -n '2,14p' "$0"
  exit 1
}

while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --lang) LANG="$2"; shift 2 ;;
    --build) BUILD="$2"; shift 2 ;;
    --run) RUN="$2"; shift 2 ;;
    --timeout) TIMEOUT="$2"; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    *) usage ;;
  esac
done

[ -n "$TARGET" ] && [ -d "$TARGET" ] || { echo "target directory required" >&2; exit 2; }
TARGET="$(cd "$TARGET" && pwd)"
command -v docker >/dev/null || { echo "docker not found" >&2; exit 2; }

case "$LANG" in
  python) IMAGE="python:3.12-slim"
          BUILD="${BUILD:-python -m compileall -q /work}"
          RUN="${RUN:-python -m unittest discover -v /work}" ;;
  node)   IMAGE="node:22-slim"
          BUILD="${BUILD:-find /work -name '*.js' -not -path '*/node_modules/*' -exec node --check {} +}"
          RUN="${RUN:-true}" ;;
  go)     IMAGE="golang:1.23"
          BUILD="${BUILD:-go build ./...}"
          RUN="${RUN:-go test -race ./...}" ;;
  rust)   IMAGE="rust:1.83"
          BUILD="${BUILD:-cargo build --offline}"
          RUN="${RUN:-cargo test --offline}" ;;
  c)      IMAGE="gcc:14"
          BUILD="${BUILD:-sh -c 'i=0; for f in /work/*.c; do [ -e \"\$f\" ] || continue; gcc -g -O1 -fsanitize=address,undefined -fno-omit-frame-pointer -o \"/work/t\$i\" \"\$f\" || exit 1; i=\$((i+1)); done'}"
          RUN="${RUN:-sh -c 'for b in /work/t*; do [ -x \"\$b\" ] || continue; echo \"== \$b\"; timeout 60 \"\$b\" || true; done'}" ;;
  *) echo "lang: python|node|go|rust|c" >&2; exit 2 ;;
esac

CMD="set -e; cp -a /src/. /work/ 2>/dev/null || true; cd /work; printf '%s\\n' '--- build ---'; $BUILD; printf '%s\\n' '--- run ---'; timeout $TIMEOUT $RUN"

echo "image: $IMAGE" >&2
echo "target: $TARGET (read-only)" >&2
echo "build: $BUILD" >&2
echo "run: $RUN" >&2

if [ "$DRY" = "1" ]; then
  echo "docker run --rm --network none --read-only --tmpfs /work:rw,exec,size=1g --tmpfs /tmp:rw,size=256m -v \"$TARGET:/src:ro\" --cap-drop ALL --security-opt no-new-privileges --pids-limit 256 --memory 1g --cpus 1 -w /work \"$IMAGE\" sh -c \"$CMD\""
  exit 0
fi

docker run --rm --network none --read-only \
  --tmpfs /work:rw,exec,size=1g --tmpfs /tmp:rw,size=256m \
  -v "$TARGET:/src:ro" \
  --cap-drop ALL --security-opt no-new-privileges \
  --pids-limit 256 --memory 1g --cpus 1 \
  -w /work "$IMAGE" sh -c "$CMD"
