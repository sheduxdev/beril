---
id: consensus-paxos
title: Paxos is prepare and accept with a ballot
tags: distributed, paxos, ballot
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Paxos is prepare and accept with a ballot

## Claim

A proposer needs a majority promise before an accept. A higher ballot supersedes. Multi-Paxos elects a stable leader.

## Test

Run two proposers with increasing ballots. Check the chosen value and the promise set.

## Proof

One value chosen despite contention.

## Failure modes

A promise is not a commit. A leader without a lease can stall.
