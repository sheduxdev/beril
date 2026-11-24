---
id: eng-concurrency
title: Concurrency bugs are about shared state and ordering
tags: engineering, concurrency, locks
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Concurrency bugs are about shared state and ordering

## Claim

A lock, an atomic or a queue protects a shared invariant. A check outside the lock is not protected.

## Test

Find the invariant. Draw the interleaving. Test with many workers.

## Proof

The invariant holds under parallel load.

## Failure modes

A lock that is too broad hides a design problem. A lock that is too narrow races.
