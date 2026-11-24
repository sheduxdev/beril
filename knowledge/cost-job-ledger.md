---
id: cost-job-ledger
title: Every job has an actor and a cost
tags: process, cost, jobs
confidence: high
updated: 2026-11-24
uses: 0
sources: data/llm_prices.json, docs/dashboard.md
status: active
---
# Every job has an actor and a cost

## Claim

Work without a ledger cannot be budgeted. A job records type, actor, model, tokens, cost and status.

## Test

Start a job, do the work, finish it with tokens or a cost. Review the monthly total against the budget.

## Proof

A job row with a cost and a finished timestamp.

## Failure modes

A model without a price is zero. Add the rate before trusting the total.
