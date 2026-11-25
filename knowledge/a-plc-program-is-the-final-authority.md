---
id: a-plc-program-is-the-final-authority
title: A PLC program is the final authority
tags: ot, plc, logic
confidence: high
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# A PLC program is the final authority

## Claim

A register write can be overwritten by the scan cycle. The proof needs the program state, not one read.

## Test

Read the program or the cross reference. Pick a point with no write in the logic. Write and sample over several cycles.

## Proof

A value that survives the scan cycle.

## Failure modes

A watchdog can reset the point. A redundant PLC can take over.
