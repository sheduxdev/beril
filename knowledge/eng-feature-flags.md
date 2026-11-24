---
id: eng-feature-flags
title: A feature flag is a temporary branch with an owner
tags: engineering, feature-flag, release
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A feature flag is a temporary branch with an owner

## Claim

A flag lets code ship before it is on. A flag without an expiry becomes permanent complexity.

## Test

Name the owner, the default and the removal date. Test both states.

## Proof

A flag with a removal ticket.

## Failure modes

A flag that controls a schema or a security check is a liability.
