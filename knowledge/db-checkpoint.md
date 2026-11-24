---
id: db-checkpoint
title: A checkpoint bounds the recovery work
tags: database, checkpoint, recovery
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A checkpoint bounds the recovery work

## Claim

The checkpoint flushes dirty pages and records a log position. Recovery starts from there.

## Test

Take checkpoints under load. Kill the process. Measure the replay length.

## Proof

A recovery time inside the target.

## Failure modes

A checkpoint that blocks writes causes a spike. A lazy checkpoint lengthens recovery.
