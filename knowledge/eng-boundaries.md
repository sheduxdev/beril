---
id: eng-boundaries
title: A boundary hides a decision and owns its data
tags: engineering, architecture, boundaries
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A boundary hides a decision and owns its data

## Claim

A good boundary has a contract, a data owner and a failure mode. A layer that calls through is not a boundary.

## Test

List the decisions each module owns. Find a change that crosses three modules. Move one decision behind the boundary.

## Proof

A change local to one module with a stable contract.

## Failure modes

A shared database makes two services one boundary.
