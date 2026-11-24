---
id: db-join-algorithms
title: Join choice is a cost model over sizes and order
tags: database, join, query
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Join choice is a cost model over sizes and order

## Claim

Nested loop is cheap for a small outer, hash for an equi-join with memory, merge for sorted input.

## Test

Read the plan. Compare a nested loop and a hash join on the same data.

## Proof

The cheaper plan with the expected row count.

## Failure modes

A hash join spills on a bad estimate. A merge join stalls on unsorted input.
