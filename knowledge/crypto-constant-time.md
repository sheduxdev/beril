---
id: crypto-constant-time
title: Secret-dependent branches leak through timing
tags: cryptography, constant-time, timing
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Secret-dependent branches leak through timing

## Claim

A compare that returns on the first mismatch leaks the prefix. Constant-time code touches every byte.

## Test

Time a byte comparison over many inputs. Compare early-exit and constant-time.

## Proof

A flat timing distribution for the secret-dependent path.

## Failure modes

A compiler can reintroduce a branch. A table lookup indexed by a secret leaks the cache.
