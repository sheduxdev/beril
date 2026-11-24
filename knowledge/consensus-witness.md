---
id: consensus-witness
title: A witness votes but stores no data
tags: distributed, consensus, witness
confidence: low
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A witness votes but stores no data

## Claim

The witness adds a quorum vote with little storage. It cannot serve a snapshot or become a full replica.

## Test

Lose a data node. Check whether the witness preserves quorum and recovery limits.

## Proof

A quorum that survives one data-node loss.

## Failure modes

A witness cannot replace a failed replica. Two witnesses with one data node are fragile.
