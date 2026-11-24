---
id: eng-consensus
title: Consensus is quorum plus a log
tags: engineering, distributed, consensus
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Consensus is quorum plus a log

## Claim

A leader appends to a replicated log; a quorum acknowledges before commit. Two leaders with the same term are a split brain.

## Test

Write on the leader. Kill the leader. Check the new leader and the committed index.

## Proof

A committed write survives a leader change.

## Failure modes

A majority of one is not consensus. A stale leader can serve old reads.
