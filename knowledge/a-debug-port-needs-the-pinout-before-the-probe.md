---
id: a-debug-port-needs-the-pinout-before-the-probe
title: A debug port needs the pinout before the probe
tags: hardware, jtag, debug
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-jtag.md
status: active
---
# A debug port needs the pinout before the probe

## Claim

JTAG and SWD expose the core. A wrong pinout or voltage can halt the board or damage it, so the map comes first.

## Test

Find the pads and the ground. Measure the voltage. Scan the chain at the right level. Read an id code before a halt.

## Proof

A chain scan with a known id and one register read.

## Failure modes

A disabled port stays silent. A 1.8V target can need a level shifter.
