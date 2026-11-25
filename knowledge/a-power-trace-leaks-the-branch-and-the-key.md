---
id: a-power-trace-leaks-the-branch-and-the-key
title: A power trace leaks the branch and the key
tags: hardware, side-channel, power
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/firmware-iot.md
status: active
---
# A power trace leaks the branch and the key

## Claim

The current draw follows the executed instructions and the data. A correlated trace can recover a key without opening the code.

## Test

Trigger a known operation. Capture the power with a shunt and a scope. Average many traces. Correlate against a key guess.

## Proof

A key guess with a clear correlation peak.

## Failure modes

A decoupling capacitor hides the trace. A noisy clock needs alignment.
