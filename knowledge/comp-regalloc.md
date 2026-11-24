---
id: comp-regalloc
title: Register allocation maps live ranges to finite registers
tags: compiler, regalloc, spill
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Register allocation maps live ranges to finite registers

## Claim

Live ranges compete for a small register file. A spill moves a value to the stack.

## Test

Build an interference graph. Compare a graph-coloring and a linear-scan allocator.

## Proof

A correct allocation with a bounded spill count.

## Failure modes

A spill in a hot loop is a large slowdown. A coalescing bug miscompiles.
