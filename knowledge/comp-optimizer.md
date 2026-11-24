---
id: comp-optimizer
title: An optimization must preserve semantics
tags: compiler, optimizer, semantics
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An optimization must preserve semantics

## Claim

Constant folding, inlining and loop transforms change the shape, not the result. A test oracle is required.

## Test

Run a randomized program corpus with and without the pass. Compare output.

## Proof

Identical output across the corpus.

## Failure modes

Undefined behavior lets an optimizer do surprising things. A pass without a test is a guess.
