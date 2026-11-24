---
id: cloud-oidc-ci
title: CI OIDC trust is a subject claim match
tags: cloud, oidc, ci
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# CI OIDC trust is a subject claim match

## Claim

The cloud role trusts a repository or branch by a string match. A wildcard, a fork or a tag can satisfy it.

## Test

Read the trust policy. Compare the sub and aud claims. Run a workflow from a fork or another ref.

## Proof

Token exchange from a ref the role should not trust.

## Failure modes

A claim on repo:ref:refs/heads/main is narrow. A wildcard on repo:* is not.
