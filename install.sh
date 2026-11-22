#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOLS=0
SCAN=""

while [ $# -gt 0 ]; do
  case "$1" in
    --tools) TOOLS=1 ;;
    --scan) SCAN="${2:-}"; shift ;;
    -h|--help)
      echo "usage: ./install.sh [--tools] [--scan URL]"
      exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 1 ;;
  esac
  shift
done

cd "$ROOT"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required" >&2
  exit 1
fi

if [ ! -d .venv ]; then
  echo "[1/4] creating .venv"
  python3 -m venv .venv
fi

echo "[2/4] installing Python packages"
.venv/bin/pip install -U pip >/dev/null
.venv/bin/pip install -r requirements.txt

echo "[3/4] fetching the Camoufox browser"
.venv/bin/camoufox fetch

echo "[4/4] checking the catalog"
.venv/bin/python scripts/validate.py

if [ "$TOOLS" = "1" ]; then
  if ! command -v go >/dev/null 2>&1; then
    echo "Go is not installed. Skipping the optional recon tools." >&2
    echo "Install Go from https://go.dev/dl/ and run ./install.sh --tools again." >&2
  else
    export GOBIN="${GOBIN:-$HOME/go/bin}"
    export PATH="$GOBIN:$PATH"
    mkdir -p "$GOBIN"
    echo "installing optional Go tools into $GOBIN"
    packages=(
      github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
      github.com/projectdiscovery/httpx/cmd/httpx@latest
      github.com/projectdiscovery/katana/cmd/katana@latest
      github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
      github.com/projectdiscovery/dnsx/cmd/dnsx@latest
      github.com/projectdiscovery/tlsx/cmd/tlsx@latest
      github.com/projectdiscovery/cdncheck/cmd/cdncheck@latest
      github.com/projectdiscovery/asnmap/cmd/asnmap@latest
      github.com/projectdiscovery/alterx/cmd/alterx@latest
      github.com/projectdiscovery/notify/cmd/notify@latest
      github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest
      github.com/projectdiscovery/uncover/cmd/uncover@latest
      github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
      github.com/ffuf/ffuf/v2@latest
      github.com/lc/gau/v2/cmd/gau@latest
      github.com/tomnomnom/waybackurls@latest
      github.com/tomnomnom/assetfinder@latest
      github.com/OJ/gobuster/v3@latest
      github.com/tomnomnom/hakrawler@latest
      github.com/zricethezav/gitleaks/v8@latest
      github.com/aquasecurity/trivy/cmd/trivy@latest
    )
    for pkg in "${packages[@]}"; do
      echo "  $pkg"
      go install "$pkg"
    done
    if command -v nuclei >/dev/null 2>&1; then
      nuclei -update-templates || true
    fi
    echo "installing semgrep into the Beril environment"
    .venv/bin/pip install semgrep || true
    echo "Add this to your shell profile if needed:"
    echo "  export PATH=\"$GOBIN:\$PATH\""
    echo "Optional reverse-engineering tools:"
    if command -v pacman >/dev/null 2>&1; then
      echo "  sudo pacman -S apktool jadx"
    elif command -v apt-get >/dev/null 2>&1; then
      echo "  sudo apt install apktool jadx"
    fi
    echo "  pip install frida-tools objection"
  fi
fi

if [ -n "$SCAN" ]; then
  echo "scanning $SCAN"
  ./beril scan --target "$SCAN" --out "scans/$(echo "$SCAN" | sed 's#https\?://##; s#[/:]#_#g')"
fi

echo
echo "Beril is ready."
echo "  ./beril scan --target https://your-app.example"
echo "  ./beril harvest forums --sources 0x00sec,reddit"
echo "  ./beril dossier"
