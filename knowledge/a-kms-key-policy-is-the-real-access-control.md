---
id: a-kms-key-policy-is-the-real-access-control
title: A KMS key policy is the real access control
tags: cloud, kms, policy
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-secrets.md
status: active
---
# A KMS key policy is the real access control

## Claim

IAM on the key is useless if the key policy grants a principal. The policy is the root of trust.

## Test

Read the key policy. Compare with the IAM policy. Try decrypt with a principal the policy allows.

## Proof

A decrypt with a principal outside the intended role.

## Failure modes

A key policy with a strict service principal holds. A grants model can add access.
