---
id: eng-team-topology
title: Team boundaries shape the architecture
tags: engineering, team, ownership
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Team boundaries shape the architecture

## Claim

A service owned by three teams has three priorities. Ownership follows the boundary, not the org chart.

## Test

Map services to owners. Find a service with more than one owner.

## Proof

One owner and one on-call rotation per boundary.

## Failure modes

A shared database blurs ownership. A platform team can own a shared capability.
