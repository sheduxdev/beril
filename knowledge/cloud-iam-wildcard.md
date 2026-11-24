---
id: cloud-iam-wildcard
title: IAM wildcard is administrator access until proven otherwise
tags: cloud, iam, aws
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# IAM wildcard is administrator access until proven otherwise

## Claim

A role or user has Action:* or a broad service wildcard, often on Resource:*. A leaked credential is domain admin in the account.

## Test

Get caller identity. Enumerate policy. Test one read outside the intended service. Look for iam:PassRole or sts:AssumeRole.

## Proof

A read-only call that returns data the role should not reach, or a role assumption.

## Failure modes

A role name is not a permission. Conditions and permission boundaries can narrow it.
