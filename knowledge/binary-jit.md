---
id: binary-jit
title: JIT bugs are about generated code and stale metadata
tags: binary, jit, exploit
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/exploit-development.md
status: active
---
# JIT bugs are about generated code and stale metadata

## Claim

A JIT emits code into RWX or W^X pages and trusts types or bounds that can change after optimization.

## Test

Map the JIT entry. Compare optimized and unoptimized behavior. Look for type confusion across deopt.

## Proof

A controlled read/write or a call to a controlled address.

## Failure modes

A JIT crash without a type bug is not enough. Deoptimization matters.
