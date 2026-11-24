---
id: formal-invariant
title: An invariant is true before and after every step
tags: formal, invariant, proof
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An invariant is true before and after every step

## Claim

The invariant constrains the state; the proof shows each transition preserves it. A broken invariant is the bug.

## Test

Write the invariant. Try a transition that violates it. Check the proof obligation.

## Proof

A transition that preserves the invariant or a counterexample.

## Failure modes

An invariant that restates the code proves nothing. A missing precondition hides a case.
