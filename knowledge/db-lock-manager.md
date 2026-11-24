---
id: db-lock-manager
title: A lock manager has modes, a wait queue and fairness
tags: database, locks, fairness
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A lock manager has modes, a wait queue and fairness

## Claim

Shared and exclusive modes conflict by a matrix. The wait queue needs ordering and timeout.

## Test

Request conflicting modes from two sessions. Check the queue and the timeout.

## Proof

A predictable grant order and a clean timeout.

## Failure modes

A lock upgrade can deadlock. A queue without fairness starves.
