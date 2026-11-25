---
id: jtag-can-halt-the-core
title: JTAG can halt the core
tags: firmware, jtag, debug
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-jtag.md
status: active
---
# JTAG can halt the core

## Claim

An open JTAG port lets the debugger halt the CPU and read memory, which bypasses the running firmware checks.

## Test

Find the header or the pads. Scan the chain with a debugger. Halt and read a known address.

## Proof

A halted core and a memory read.

## Failure modes

A fused off port stays silent. A secure debug unlock can need a key.
