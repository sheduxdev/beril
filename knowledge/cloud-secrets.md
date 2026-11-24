---
id: cloud-secrets
title: A secrets manager is only as strong as its policy
tags: cloud, secrets, iam
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# A secrets manager is only as strong as its policy

## Claim

The secret policy allows a broad principal, cross-account trust, or a role the workload does not need.

## Test

Read the resource policy. Test with the workload role and a second role. Check rotation.

## Proof

A read by a principal outside the intended workload.

## Failure modes

A secret encrypted with a default key is still readable by a policy mistake. Rotation alone is not access control.
