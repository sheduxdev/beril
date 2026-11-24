---
id: comp-instr-select
title: Instruction selection matches IR trees to target patterns
tags: compiler, codegen, isel
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Instruction selection matches IR trees to target patterns

## Claim

The selector rewrites IR shapes into machine instructions, preferring a single instruction when one covers the tree.

## Test

Feed a pattern that has a fused instruction. Compare with a naive lowering.

## Proof

The fused instruction with correct flags.

## Failure modes

A pattern that ignores side effects reorders a load. A cost model can pick a worse pattern.
