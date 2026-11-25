---
id: coverage-guided-fuzzing-needs-the-right-build
title: Coverage guided fuzzing needs the right build
tags: fuzz, coverage, build
confidence: high
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# Coverage guided fuzzing needs the right build

## Claim

Without sanitizer coverage and a debug build the fuzzer is blind and crashes are harder to triage.

## Test

Build with the fuzzer flags and ASAN. Check the map size and the stability. Run a short campaign.

## Proof

A rising edge count and a reproducible crash.

## Failure modes

A stripped release build hides both. A static link can block the sanitizer.
