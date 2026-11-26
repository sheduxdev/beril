#!/usr/bin/env bash
# Smoke tests for the hardware lab artifacts.
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

check "baud" "115200" "uart.log"
check "root shell" "sample shell#" "uart.log"
check "device key" "hw-lab-9a7c" "uart.log"
check "flash key" "hw-flash-9a7c" "spi_dump.txt"
check "clear update url" "http://updates.legacy.example" "spi_dump.txt"
check "secure boot blown" "SECURE_BOOT_ENABLE = BLOWN" "fuse_map.txt"
check "jtag open" "JTAG_ENABLE = OPEN" "fuse_map.txt"
check "uart pads" "TP3 UART_TX" "pcb_notes.txt"
check "rollback counter" "anti_rollback_counter 7" "update_manifest.txt"

echo "---"
echo "pass=$PASS fail=$FAIL"
[ "$FAIL" = "0" ]
