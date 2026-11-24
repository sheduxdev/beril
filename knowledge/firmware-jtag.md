---
id: firmware-jtag
title: JTAG and SWD are identified by pinout and IDCODE
tags: firmware, hardware, jtag
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/firmware-iot.md
status: active
---
# JTAG and SWD are identified by pinout and IDCODE

## Claim

The board exposes a debug header. The TAP or SWD IDCODE identifies the target and allows a flash dump.

## Test

Find TMS/TCK/TDI/TDO or SWDIO/SWCLK. Use OpenOCD with a target config. Read the IDCODE before dumping.

## Proof

A flash dump that matches a second read.

## Failure modes

A header that looks like JTAG can be unpopulated or disabled. Read the chip datasheet.
