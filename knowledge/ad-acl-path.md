---
id: ad-acl-path
title: AD compromise is an edge path, not a single bug
tags: ad, windows, acl
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md, labs/ad
status: active
---
# AD compromise is an edge path, not a single bug

## Claim

A user has a right over an object that leads to another right, then to a session on a high-value host.

## Test

Collect with BloodHound. Read the ACL edges. Pick the shortest path to the objective and prove one edge.

## Proof

A password reset, ticket or session that grants the next node, with the path in BloodHound.

## Failure modes

A roastable account with a strong password is not a finding until cracked. A path that needs DA to start is circular.
