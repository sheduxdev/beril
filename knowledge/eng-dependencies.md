---
id: eng-dependencies
title: Every dependency is a maintenance contract
tags: engineering, dependencies, supply-chain
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Every dependency is a maintenance contract

## Claim

A dependency adds upgrade cost, attack surface and a license. Pin it, test it and know why it exists.

## Test

List direct dependencies. Find unused ones. Check the license and the last release.

## Proof

A smaller dependency set with a lockfile.

## Failure modes

A transitive dependency is still your dependency.
