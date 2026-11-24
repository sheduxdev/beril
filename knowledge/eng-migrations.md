---
id: eng-migrations
title: A migration is expand, backfill, switch, contract
tags: engineering, database, migration
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A migration is expand, backfill, switch, contract

## Claim

The old and new schema must coexist during deploy. A rename in one step breaks a rolling deploy.

## Test

Write the four steps. Test a rollback. Check old and new code together.

## Proof

A deploy with no downtime and a reversible path.

## Failure modes

A backfill without a throttle can lock the table.
