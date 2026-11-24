---
id: db-deadlock
title: A deadlock is a cycle in the wait-for graph
tags: database, deadlock, retry
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A deadlock is a cycle in the wait-for graph

## Claim

The detector finds a cycle, picks a victim and aborts it. The client must retry the whole transaction.

## Test

Create a two-session cycle. Check the victim and the error code.

## Proof

A clear deadlock error and a successful retry.

## Failure modes

A retry inside the same transaction may repeat the partial work.
