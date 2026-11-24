---
id: storage-replication
title: Replication has a lag and a loss window
tags: storage, replication, failover
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Replication has a lag and a loss window

## Claim

Async replicas lag; failover to a lagging replica loses the tail. Sync replicas cost latency.

## Test

Measure lag under load. Fail over. Compare the last committed key.

## Proof

A failover with a stated loss window.

## Failure modes

A replica that is up is not caught up. A sync quorum can block writes.
