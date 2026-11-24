---
id: db-mvcc
title: MVCC keeps versions for concurrent snapshots
tags: database, mvcc, snapshot
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# MVCC keeps versions for concurrent snapshots

## Claim

A writer creates a new version; readers see a snapshot. Vacuum removes versions no snapshot can see.

## Test

Open a long transaction. Update the row in another session. Read both snapshots.

## Proof

The old version visible to the old snapshot and the new visible to the new one.

## Failure modes

A long snapshot blocks vacuum and bloats the table.
