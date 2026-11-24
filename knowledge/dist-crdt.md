---
id: dist-crdt
title: A CRDT merges without coordination
tags: distributed, crdt, merge
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A CRDT merges without coordination

## Claim

Counters, sets and sequences with a join rule converge. The data type carries the merge.

## Test

Apply concurrent updates on two replicas. Merge. Check convergence and intent.

## Proof

The same state on both replicas.

## Failure modes

A CRDT can lose intent: a remove-wins set loses an add. The type choice matters.
