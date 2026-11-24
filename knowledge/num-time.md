---
id: num-time
title: A timestamp is an instant; a local time is a rule
tags: numerics, time, timezone
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A timestamp is an instant; a local time is a rule

## Claim

Store UTC instants, convert at the edge with a zone database. DST and leap seconds are rules, not offsets.

## Test

Schedule across a DST change. Compare the instant and the local label.

## Proof

A schedule that fires once at the intended local time.

## Failure modes

A stored local time without a zone is ambiguous. A fixed offset breaks on DST.
