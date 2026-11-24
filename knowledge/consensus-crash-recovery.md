---
id: consensus-crash-recovery
title: Recovery replays the log to the commit index, not past it
tags: distributed, consensus, recovery
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Recovery replays the log to the commit index, not past it

## Claim

A restarted node loads the snapshot, replays committed entries and truncates uncommitted ones.

## Test

Kill a follower after an append but before commit. Restart. Compare the index.

## Proof

The node rejoins at the committed index with no duplicate.

## Failure modes

A commit index that is not durable can commit twice. A snapshot without truncation diverges.
