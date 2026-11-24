---
id: stream-exactly-once
title: Exactly-once output is a transaction or an idempotent sink
tags: data, streaming, exactly-once
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Exactly-once output is a transaction or an idempotent sink

## Claim

The sink commits with the checkpoint, or the write is keyed and idempotent. The source replays from the checkpoint.

## Test

Kill the job after a sink write but before the checkpoint. Restart. Count the outputs.

## Proof

One output per input event after recovery.

## Failure modes

A non-transactional sink duplicates on replay. A transactional sink needs a two-phase commit.
