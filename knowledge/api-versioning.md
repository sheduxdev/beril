---
id: api-versioning
title: Old API versions keep old authorization
tags: api, versioning, shadow
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Old API versions keep old authorization

## Claim

A deprecated path is still routed, with weaker auth or no schema. Clients keep it alive.

## Test

Compare v1 with v2 on the same object. Call v1 with a low-privilege token. Check the changelog.

## Proof

A v1 path returns data that v2 protects.

## Failure modes

A version that returns 410 is retired. A redirect to v2 is not a bypass.
