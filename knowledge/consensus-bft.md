---
id: consensus-bft
title: BFT assumes f faulty nodes and 3f+1 votes
tags: distributed, bft, byzantine
confidence: low
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# BFT assumes f faulty nodes and 3f+1 votes

## Claim

Byzantine nodes can lie. The quorum must be 2f+1 of 3f+1 to tolerate f liars.

## Test

Run a four-node BFT cluster with one liar. Check commit and view change.

## Proof

A commit that survives the liar.

## Failure modes

A crash-fault quorum is not BFT. Message cost grows with node count.
