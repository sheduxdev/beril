---
id: db-isolation
title: Isolation levels allow different anomalies
tags: database, isolation, write-skew
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Isolation levels allow different anomalies

## Claim

Read committed permits write skew; serializable prevents it with predicates or locks. The tradeoff is concurrency.

## Test

Run two transactions that read a predicate and write the complement. Repeat under each level.

## Proof

The anomaly or the serialization failure.

## Failure modes

A snapshot isolation label does not prevent write skew. Retry is part of serializable.
