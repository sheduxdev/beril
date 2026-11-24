---
id: db-pitr
title: Point-in-time recovery needs a base backup and WAL
tags: database, pitr, wal
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Point-in-time recovery needs a base backup and WAL

## Claim

The base backup plus the WAL segment set restores to a timestamp. Retention is the limit.

## Test

Restore to a timestamp before a bad migration. Check the row.

## Proof

A recovered database at the target timestamp.

## Failure modes

A missing WAL segment breaks the chain. A restore without a test is a guess.
