---
id: aslr-partial-overwrite-keeps-the-high-bytes
title: ASLR partial overwrite keeps the high bytes
tags: binary, aslr, partial-overwrite
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# ASLR partial overwrite keeps the high bytes

## Claim

A one or two byte overwrite of a saved pointer keeps the randomized high bytes and lands inside the same mapping with only a small brute force.

## Test

Find a pointer with a known low layout. Overwrite the last byte or two. Repeat and record the hit rate.

## Proof

Control flow reaches the chosen gadget in a stable share of runs.

## Failure modes

A page aligned target needs more bytes. Full RELRO and PIE with a large random gap lower the odds.
