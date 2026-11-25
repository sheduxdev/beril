---
id: a-public-principal-is-wider-than-a-public-acl
title: A public principal is wider than a public ACL
tags: cloud, storage, iam
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-iam-wildcard.md
status: active
---
# A public principal is wider than a public ACL

## Claim

A bucket policy that allows `*` as principal grants every AWS account, not only anonymous users, and often includes write.

## Test

Read the policy principal and actions. Try an unauthenticated read and a write from a second account.

## Proof

A second account or an anonymous client writes the object.

## Failure modes

A condition on source VPC or account narrows it. Block Public Access can be on and still show the policy.
