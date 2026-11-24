---
id: eng-simplicity
title: Simplicity is removing accidental complexity
tags: engineering, design, simplicity
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Simplicity is removing accidental complexity

## Claim

Most complexity comes from the solution: extra layers, flags, abstractions and copies. Essential complexity is the problem itself.

## Test

Name each abstraction and the decision it hides. Remove one that only forwards calls. Measure the diff.

## Proof

A smaller diff with the same behavior and fewer concepts.

## Failure modes

Clever compression can hide complexity. The reader matters.
