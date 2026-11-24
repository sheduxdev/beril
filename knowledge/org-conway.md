---
id: org-conway
title: The org chart leaks into the architecture
tags: organization, conway, law, ownership, service, teams
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# The org chart leaks into the architecture

## Claim

Conway's law says teams ship their communication structure. A boundary with three owners becomes a distributed monolith.

## Test

Map services to teams. Find a service with more than one owner or a team with ten services.

## Proof

One owner and one on-call per boundary.

## Failure modes

A platform team can own a shared capability. A matrix org blurs it.
