---
id: a-snapshot-turns-a-fuzz-crash-into-a-replay
title: A snapshot turns a fuzz crash into a replay
tags: fuzz, snapshot, replay
confidence: high
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A snapshot turns a fuzz crash into a replay

## Claim

A VM or container snapshot before the input makes a rare crash exactly reproducible.

## Test

Take the snapshot at the pre input state. Run the input. Restore and run again.

## Proof

The same crash on both runs.

## Failure modes

A snapshot can miss a hardware or a time state. A kernel ASLR change needs a fixed seed.
