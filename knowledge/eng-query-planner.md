---
id: eng-query-planner
title: The planner is the database's brain
tags: engineering, database, query
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# The planner is the database's brain

## Claim

Indexes, statistics and join order decide the plan. A missing index or a stale statistic turns a fast query slow.

## Test

Run EXPLAIN. Check the row estimate and the actual. Add the index and re-measure.

## Proof

A plan with fewer rows and a lower cost.

## Failure modes

An index on a low-selectivity column can be ignored.
