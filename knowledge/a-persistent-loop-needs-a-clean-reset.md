---
id: a-persistent-loop-needs-a-clean-reset
title: A persistent loop needs a clean reset
tags: fuzz, persistent, state
confidence: high
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A persistent loop needs a clean reset

## Claim

A persistent harness reuses the process. A leaked global or a cached pointer turns the second input into a false crash.

## Test

Run the same seed twice in one process. Compare the result. Reset the global state between iterations.

## Proof

The same result on the first and second run.

## Failure modes

A target with an intentional cache needs a fork mode. A library with a global lock can hang.
