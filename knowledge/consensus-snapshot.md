---
id: consensus-snapshot
title: A snapshot records the last included index and term
tags: distributed, raft, snapshot
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A snapshot records the last included index and term

## Claim

The snapshot metadata anchors the log position. Install sends chunks; a lagging follower catches up from the end.

## Test

Take a snapshot. Restart a follower. Kill the leader during install. Check the recovered index.

## Proof

A follower that catches up without losing a committed entry.

## Failure modes

A snapshot without the index can duplicate or skip entries. Install must not block the leader.
