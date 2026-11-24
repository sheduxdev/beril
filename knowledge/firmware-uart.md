---
id: firmware-uart
title: UART is found by idle levels and confirmed by baud
tags: firmware, hardware, uart
confidence: high
updated: 2026-11-24
uses: 0
sources: references/firmware-iot.md
status: active
---
# UART is found by idle levels and confirmed by baud

## Claim

A board exposes TX, RX and GND pads, often labeled or near the SoC. The console may drop to a shell.

## Test

Use a multimeter and logic analyzer. Find the idle-high TX pad. Try common baud rates. Do not connect VCC first.

## Proof

A console prompt or boot log on the serial line.

## Failure modes

A pad that looks like UART can be SWD. Wrong baud gives garbage. TX and RX are often crossed.
