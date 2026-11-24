---
id: num-float
title: Floating point is exact at powers of two and lossy elsewhere
tags: numerics, float, rounding
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Floating point is exact at powers of two and lossy elsewhere

## Claim

Binary floating point cannot represent 0.1. Subtracting close values cancels significant digits.

## Test

Sum 0.1 ten times. Compare with 1.0. Subtract 1e16 from 1e16+1.

## Proof

A comparison that uses an epsilon or an exact decimal type.

## Failure modes

An equality check on a float is a bug. A large sum accumulates error unless compensated.
