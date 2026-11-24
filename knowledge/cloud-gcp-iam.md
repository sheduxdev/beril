---
id: cloud-gcp-iam
title: GCP IAM binds a member to a role on a resource
tags: cloud, gcp, iam
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# GCP IAM binds a member to a role on a resource

## Claim

A service account has a primitive role or a bucket-level binding that reaches other projects, or workload identity is too broad.

## Test

Get the token. List the IAM policy. Test storage, compute and secret access. Check the service account's keys.

## Proof

A read or token mint outside the intended project.

## Failure modes

A basic role on a single bucket is limited. Impersonation needs iam.serviceAccounts.getAccessToken.
