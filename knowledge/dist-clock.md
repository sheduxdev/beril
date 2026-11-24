---
id: dist-clock
title: Physical clocks skew; logical clocks order events
tags: distributed, clock, causality
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Physical clocks skew; logical clocks order events

## Claim

Two machines disagree about time. Lamport clocks, vector clocks and version vectors encode causality.

## Test

Write on two nodes. Compare timestamps and versions. Check the merge rule.

## Proof

A causal order that survives clock skew.

## Failure modes

Timestamp ordering can drop a concurrent write. NTP reduces skew, not causality.
