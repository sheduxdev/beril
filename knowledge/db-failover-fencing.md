---
id: db-failover-fencing
title: Fencing stops the old primary from writing
tags: database, failover, fencing
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Fencing stops the old primary from writing

## Claim

The old primary must be fenced or demoted. A split brain writes two histories.

## Test

Pause the network. Promote the replica. Resume the old primary.

## Proof

One writable primary and no divergent commits.

## Failure modes

A fence that depends on the old host is weak. A stale DNS record can route writers.
