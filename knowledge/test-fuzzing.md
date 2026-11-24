---
id: test-fuzzing
title: A fuzzer explores inputs a human would not write
tags: testing, fuzzing, corpus
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A fuzzer explores inputs a human would not write

## Claim

Coverage feedback grows the corpus. A crash is minimized to a reproducer.

## Test

Fuzz a parser for an hour. Check the coverage and the saved corpus.

## Proof

A crash with a minimal input saved to the corpus.

## Failure modes

A fuzzer without a dictionary misses magic bytes. A flaky crash without a reproducer wastes time.
