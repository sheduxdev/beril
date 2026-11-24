---
id: consensus-membership
title: Membership change is a consensus decision
tags: distributed, raft, membership
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Membership change is a consensus decision

## Claim

Changing the voter set can create two majorities. Joint consensus or one-at-a-time changes preserve overlap.

## Test

Add and remove a node while writes continue. Check the quorum and the leader.

## Proof

A config change with no split brain and no lost commit.

## Failure modes

A two-node change in one step can overlap two majorities.
