---
id: eng-api-versioning
title: A version is a deprecation clock
tags: engineering, api, versioning
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A version is a deprecation clock

## Claim

Breaking changes need a new version and a sunset date. Additive changes stay in the current version.

## Test

Diff the contract. Classify breaking. Set the sunset and the telemetry.

## Proof

A version with a migration guide and a usage metric.

## Failure modes

A version nobody calls is dead weight. A breaking change in place is a surprise.
