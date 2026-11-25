---
id: graphql-aliases-turn-one-request-into-many
title: GraphQL aliases turn one request into many
tags: api, graphql, rate-limit
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/api-batch.md, references/techniques.md
status: active
---
# GraphQL aliases turn one request into many

## Claim

A single query with many aliases repeats a resolver under one rate limit slot and can brute force or amplify load.

## Test

Send the same field one hundred times under aliases with different arguments. Compare time and quota use.

## Proof

One request performs one hundred lookups.

## Failure modes

A query cost analyzer blocks it. A resolver cache absorbs repeats.
