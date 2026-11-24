---
id: trace-cardinality
title: A span attribute multiplies the index size
tags: observability, cardinality, tracing
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A span attribute multiplies the index size

## Claim

A user id or a raw URL as an attribute explodes the distinct values. A bounded set stays queryable.

## Test

Count distinct values per attribute. Drop the worst offender.

## Proof

An attribute set with a bounded cardinality.

## Failure modes

A high-cardinality attribute makes the backend expensive and slow. A missing attribute loses the join.
