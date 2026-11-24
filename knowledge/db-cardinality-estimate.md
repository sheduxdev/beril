---
id: db-cardinality-estimate
title: Estimates decide the plan; bad estimates ruin it
tags: database, cardinality, planner
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Estimates decide the plan; bad estimates ruin it

## Claim

Histograms and stats predict rows. A correlated predicate or a stale stat produces a 1-row guess for 1M rows.

## Test

Compare EXPLAIN estimate with actual. Update stats. Test a correlated predicate.

## Proof

An estimate within an order of magnitude and a better plan.

## Failure modes

An estimate that is wrong by 1000x picks a nested loop. Sampling helps, correlation does not.
