---
id: consensus-linearizable-read
title: A linearizable read needs a leader lease or a read index
tags: distributed, consensus, read
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A linearizable read needs a leader lease or a read index

## Claim

Reading from a follower can be stale. A read index confirms the leader's commit index; a lease bounds staleness.

## Test

Read from a follower under partition. Check the value and the lease expiry.

## Proof

The latest committed value or a clear refusal.

## Failure modes

A clock-based lease can expire early. A stale read is invisible without a version.
