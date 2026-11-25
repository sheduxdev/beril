---
id: a-cloud-role-trust-to-a-repo-needs-the-ref-and-the-environme
title: A cloud role trust to a repo needs the ref and the environment
tags: supply, oidc, trust
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-oidc-ci.md
status: active
---
# A cloud role trust to a repo needs the ref and the environment

## Claim

Without a ref and environment condition, any workflow in the repo can assume the deployment role, including a fork pull request.

## Test

Read the trust policy. Run a workflow from a branch and from a fork. Compare the token claims.

## Proof

An untrusted ref assumes the role.

## Failure modes

A protected environment and a tag rule close it. A read only role limits the impact.
