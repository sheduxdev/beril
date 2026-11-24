---
id: dist-backfill
title: A backfill is a throttled repair stream
tags: distributed, backfill, repair
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A backfill is a throttled repair stream

## Claim

Missing data is replayed from a source while live traffic continues. A throttle and a checkpoint keep it safe.

## Test

Backfill a lagging replica. Measure the source and the replica load. Stop and resume.

## Proof

A caught-up replica without a source overload.

## Failure modes

An unthrottled backfill competes with live traffic. A checkpoint that is not durable repeats work.
