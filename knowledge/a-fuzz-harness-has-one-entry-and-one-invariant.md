---
id: a-fuzz-harness-has-one-entry-and-one-invariant
title: A fuzz harness has one entry and one invariant
tags: fuzz, harness, entry
confidence: high
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A fuzz harness has one entry and one invariant

## Claim

A useful harness reaches the parser with bytes and checks one property. A harness that skips the parser only fuzzes the wrapper.

## Test

Read the target function. Write the smallest main that passes the buffer. Assert the return and the length invariant.

## Proof

The harness reaches the parser and a mutation changes the path.

## Failure modes

A harness that validates input before the target filters the corpus. A global state target needs a reset.
