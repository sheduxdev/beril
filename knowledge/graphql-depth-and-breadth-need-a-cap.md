---
id: graphql-depth-and-breadth-need-a-cap
title: GraphQL depth and breadth need a cap
tags: api, graphql, dos
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/api-batch.md
status: active
---
# GraphQL depth and breadth need a cap

## Claim

A recursive fragment or a wide connection graph can exhaust the server before any field returns.

## Test

Build a self referencing fragment to depth 20. Then request many connections with large first values.

## Proof

The request times out or the response is much slower than a shallow one.

## Failure modes

Depth and complexity limits are common. Measure against a baseline before calling it a bug.
