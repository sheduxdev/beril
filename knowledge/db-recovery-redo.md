---
id: db-recovery-redo
title: Redo applies committed pages before undo
tags: database, recovery, redo
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Redo applies committed pages before undo

## Claim

Crash recovery replays the log to a consistent point, then rolls back uncommitted transactions.

## Test

Kill the process mid-write. Restart. Check the redo and undo order.

## Proof

A consistent database with the committed row.

## Failure modes

A wrong order resurrects uncommitted data. A torn page needs a checksum.
