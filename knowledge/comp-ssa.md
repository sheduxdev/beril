---
id: comp-ssa
title: SSA makes each definition single and explicit
tags: compiler, ssa, dataflow
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# SSA makes each definition single and explicit

## Claim

Static single assignment gives every value one definition and uses phi nodes at joins. Dataflow becomes a graph walk.

## Test

Convert a small CFG to SSA. Name the phi nodes. Check the def-use chains.

## Proof

A correct SSA form with no duplicate defs.

## Failure modes

A phi missing at a join is a miscompile. Dominance matters.
