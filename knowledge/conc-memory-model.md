---
id: conc-memory-model
title: The memory model defines which writes a read may see
tags: concurrency, memory-model, atomics
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# The memory model defines which writes a read may see

## Claim

Without synchronization, a compiler and a CPU may reorder. An atomic with the right ordering creates happens-before.

## Test

Run a data race under ThreadSanitizer. Add a release/acquire pair. Check the visibility.

## Proof

A race-free program with a documented ordering.

## Failure modes

A relaxed atomic does not order other accesses. A volatile flag is not a memory barrier in every language.
