---
id: an-oidc-sub-wildcard-trusts-every-branch
title: An OIDC `sub` wildcard trusts every branch
tags: cloud, oidc, ci
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-oidc-ci.md, knowledge/cicd-pr-target.md
status: active
---
# An OIDC `sub` wildcard trusts every branch

## Claim

A CI trust policy with a wildcard in the subject lets a pull request branch assume the deployment role.

## Test

Read the `sub` condition. Compare with the branch or tag rule. Run a workflow from a fork or a new branch.

## Proof

The untrusted branch gets the role.

## Failure modes

An environment or a tag restriction closes it. The role can still be read only.
