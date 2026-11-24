---
id: race-idempotency
title: A unique constraint is the cheapest race fix
tags: web, race, database
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# A unique constraint is the cheapest race fix

## Claim

The app checks for an existing row, then inserts. Two requests pass the check. A unique index or idempotency key closes it.

## Test

Send the same create request twice in parallel. Check the row count. Add a unique index and repeat.

## Proof

One row after the fix, two before it.

## Failure modes

A transaction without a unique constraint can still race at a higher isolation level. Test the real DB.
