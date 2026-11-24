---
id: ai-cost-control
title: An agent loop is a budget bug
tags: ai, cost, agent
confidence: medium
updated: 2026-11-24
uses: 0
sources: docs/dashboard.md
status: active
---
# An agent loop is a budget bug

## Claim

Retries, reflection and tool loops consume tokens without a cap. A single task can cost more than the result.

## Test

Set a token and turn budget. Log each job with tokens and cost. Stop on a plateau.

## Proof

A job ledger entry with a cost under the budget.

## Failure modes

A cheap model still loops. A budget without a stop condition is a warning only.
