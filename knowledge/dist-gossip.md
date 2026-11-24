---
id: dist-gossip
title: Gossip spreads state in logarithmic rounds
tags: distributed, gossip, membership
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Gossip spreads state in logarithmic rounds

## Claim

Each node forwards rumors to a few peers. Membership and failure detection converge without a central registry.

## Test

Simulate node loss and message loss. Measure convergence time and false failure rate.

## Proof

A stable membership view after churn.

## Failure modes

A slow gossip interval delays failover. A short one floods the network.
