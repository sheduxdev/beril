---
id: eng-security-design
title: Security is a property of the design
tags: engineering, security, design
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Security is a property of the design

## Claim

A check at the edge is not a boundary if another path reaches the data. Authorization belongs next to the data.

## Test

Draw the paths. Put the check at the narrowest boundary. Test a sibling path.

## Proof

A sibling path that cannot bypass the check.

## Failure modes

A UI check is not an authorization check.
