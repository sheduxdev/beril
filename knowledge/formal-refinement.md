---
id: formal-refinement
title: Refinement maps an abstract spec to concrete steps
tags: formal, refinement, spec
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Refinement maps an abstract spec to concrete steps

## Claim

Each concrete step must simulate an abstract step or stutter. A refinement proof preserves the spec's properties.

## Test

Write the abstraction relation. Check one concrete step against it.

## Proof

A simulation relation that holds for every step.

## Failure modes

A refinement that skips internals hides a behavior change. A weak abstraction relation proves a different system.
