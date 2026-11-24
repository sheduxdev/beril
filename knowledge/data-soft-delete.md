---
id: data-soft-delete
title: A soft delete must not break uniqueness or joins
tags: data-modeling, soft-delete, uniqueness
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A soft delete must not break uniqueness or joins

## Claim

A deleted flag keeps the row; a partial unique index admits a new row with the same key.

## Test

Delete a row and insert the same key. Check the constraint and the queries.

## Proof

A new row allowed while the deleted one stays for audit.

## Failure modes

A global unique index blocks re-creation. A query without the flag shows deleted rows.
