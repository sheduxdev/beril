---
id: cloud-alibaba-ram
title: Alibaba RAM roles and STS follow the same trust graph
tags: cloud, alibaba, ram
confidence: low
updated: 2026-11-25
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Alibaba RAM roles and STS follow the same trust graph

## Claim

A RAM role trusts an account or service, and STS issues temporary credentials. A wildcard policy crosses the boundary.

## Test

Read the role trust policy. Assume the role. Test a read outside the intended resource.

## Proof

An STS token with access beyond the role's purpose.

## Failure modes

A role name is not a permission. A policy condition can narrow it.
