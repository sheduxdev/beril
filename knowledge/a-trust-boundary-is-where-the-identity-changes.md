---
id: a-trust-boundary-is-where-the-identity-changes
title: A trust boundary is where the identity changes
tags: design, trust-boundary, identity
confidence: high
updated: 2026-11-26
uses: 0
sources: references/senior-bar.md, references/specialist-program.md
status: active
---
# A trust boundary is where the identity changes

## Claim

The boundary is the point where data or a request moves to another identity, tenant, network or privilege level. A check on one side is not a check on the other.

## Test

Mark every place the caller identity or the data owner changes. Read the check at each side. Find the side with none.

## Proof

A request that crosses the boundary without a check.

## Failure modes

A shared middleware can cover several boundaries. A network boundary can hide an app boundary.
