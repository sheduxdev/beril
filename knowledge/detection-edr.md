---
id: detection-edr
title: EDR detection is a process tree and a sequence
tags: detection, edr, process
confidence: medium
updated: 2026-11-24
uses: 0
sources: labs/detection
status: active
---
# EDR detection is a process tree and a sequence

## Claim

A single event is weak; parent-child, command line, token and network together are strong.

## Test

Map the process tree. Add command-line and network fields. Test against a normal baseline.

## Proof

A rule that catches the technique and not the baseline.

## Failure modes

A signature on a binary name is easy to evade. Behavior is stronger.
