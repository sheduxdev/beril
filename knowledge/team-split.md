---
id: team-split
title: A split needs an ownership map before the move
tags: team-scaling, split, ownership
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A split needs an ownership map before the move

## Claim

Move whole services and clear interfaces, not half of a service. The new team starts with a boundary.

## Test

Write the ownership map. Check every service has one owner.

## Proof

A split with no shared ownership.

## Failure modes

A split by layer creates a matrix. A split during an incident is chaos.
