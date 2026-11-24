---
id: comp-ub
title: Undefined behavior lets the optimizer assume
tags: compiler, ub, optimizer
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Undefined behavior lets the optimizer assume

## Claim

Signed overflow, strict aliasing and null dereference let the compiler remove checks. The source can look safe.

## Test

Compile at -O2 with UBSAN. Compare the branch with -O0. Trigger the assumption.

## Proof

A sanitizer report or a behavior change across optimization levels.

## Failure modes

A test at -O0 can pass while production breaks.
