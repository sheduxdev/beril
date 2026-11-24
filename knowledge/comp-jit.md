---
id: comp-jit
title: A JIT has tiers, guards and a code cache
tags: compiler, jit, deopt
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A JIT has tiers, guards and a code cache

## Claim

Fast code depends on assumptions. A guard fails and the runtime deopts to a slower tier.

## Test

Read the tier policy and the guards. Force a deopt. Check the code cache.

## Proof

A correct result across the deopt.

## Failure modes

A JIT bug can appear only after warmup. Code cache invalidation matters.
