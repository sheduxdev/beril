---
id: formal-tla
title: TLA+ describes a protocol as state and actions
tags: formal, tla, protocol
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# TLA+ describes a protocol as state and actions

## Claim

The spec is a state machine with invariants and temporal properties. The model checker explores it.

## Test

Specify a leader election. Check that two leaders never coexist. Run TLC.

## Proof

A checked invariant or a trace.

## Failure modes

A spec with a weak fairness assumption hides a liveness bug. The mapping to code is manual.
