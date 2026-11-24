---
id: consensus-pre-vote
title: Pre-vote stops a rejoining node from disrupting the leader
tags: distributed, raft, election
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Pre-vote stops a rejoining node from disrupting the leader

## Claim

A node with a stale term asks for votes before incrementing. A majority pre-vote prevents term inflation.

## Test

Partition a follower, restart it, rejoin. Watch the leader term.

## Proof

The leader stays stable through the rejoin.

## Failure modes

Pre-vote without a timeout can stall. A partition that heals mid-vote is subtle.
