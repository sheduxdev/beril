---
id: repair-hinted-handoff
title: A hinted handoff parks a write and replays it later
tags: distributed-storage, hinted, handoff, replay, repair
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A hinted handoff parks a write and replays it later

## Claim

The coordinator stores a hint with a TTL. The replay must be bounded and idempotent.

## Test

Write while a replica is down. Restart it. Check the hint replay and the duplicate handling.

## Proof

One applied write and a drained hint.

## Failure modes

An unbounded hint store grows. A replay that is not idempotent doubles the write.
