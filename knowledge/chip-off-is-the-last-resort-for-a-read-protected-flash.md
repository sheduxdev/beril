---
id: chip-off-is-the-last-resort-for-a-read-protected-flash
title: Chip off is the last resort for a read protected flash
tags: hardware, emmc, chip-off
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/firmware-iot.md
status: active
---
# Chip off is the last resort for a read protected flash

## Claim

When a clip and a debug port fail, removing the eMMC or the NAND and reading it in a socket bypasses the CPU.

## Test

Identify the package. Reflow the chip with a hot air station. Read in a socket. Reball and refit.

## Proof

A dump with a filesystem.

## Failure modes

A BGA reball can fail. An encrypted filesystem needs the key from the CPU.
