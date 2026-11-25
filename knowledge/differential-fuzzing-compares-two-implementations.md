---
id: differential-fuzzing-compares-two-implementations
title: Differential fuzzing compares two implementations
tags: fuzz, differential, parser
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# Differential fuzzing compares two implementations

## Claim

Two parsers for the same format should agree. A divergence is a bug in one of them, and the oracle is free.

## Test

Feed the same bytes to both. Compare the output, the error and the timing. Minimize the divergence.

## Proof

A minimal input where the two differ.

## Failure modes

A documented difference makes noise. A shared library can hide the divergence.
