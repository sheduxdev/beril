---
id: eng-cqrs
title: CQRS separates the write model from the read model
tags: engineering, cqrs, read-model
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# CQRS separates the write model from the read model

## Claim

The write side enforces invariants; the read side is denormalized for queries. The gap is eventual consistency.

## Test

Measure the projection lag. Read after a write. Test the UI with the lag.

## Proof

A read model that converges and a UI that handles the gap.

## Failure modes

A shared table with two names is not CQRS. A lag without a UI story is a bug.
