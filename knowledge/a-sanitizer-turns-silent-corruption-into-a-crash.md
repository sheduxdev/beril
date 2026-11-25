---
id: a-sanitizer-turns-silent-corruption-into-a-crash
title: A sanitizer turns silent corruption into a crash
tags: fuzz, sanitizer, asan
confidence: high
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A sanitizer turns silent corruption into a crash

## Claim

ASAN, UBSAN and MSAN catch overflows, undefined behavior and uninitialized reads that do not crash on their own.

## Test

Build with the sanitizer. Run the corpus. Compare crashes with and without.

## Proof

A sanitizer report with a stack and the input.

## Failure modes

A sanitizer changes layout and timing. A false positive can come from a deliberate pattern.
