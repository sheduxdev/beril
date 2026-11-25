---
id: a-campaign-is-a-shared-time-and-infrastructure
title: A campaign is a shared time and infrastructure
tags: ti, campaign, cluster
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/vulnerability-research.md
status: active
---
# A campaign is a shared time and infrastructure

## Claim

A campaign groups activity by shared infrastructure, tooling and window. A shared hash alone can be a common loader.

## Test

List the infrastructure and the time window. Compare with the tool overlap. Remove the common tool and see what remains.

## Proof

A cluster with independent links beyond one tool.

## Failure modes

A shared hosting node can join two actors. A long campaign can change tools.
