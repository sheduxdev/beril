---
id: formal-model-check
title: Model checking enumerates states until a property fails
tags: formal, model-check, states
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Model checking enumerates states until a property fails

## Claim

The tool explores the transition graph. State explosion is the limit; abstraction and symmetry reduce it.

## Test

Model a two-process lock. Ask for mutual exclusion. Check the counterexample trace.

## Proof

A verified property or a concrete trace to the violation.

## Failure modes

A model that omits a transition proves a smaller system. A state space too large times out.
