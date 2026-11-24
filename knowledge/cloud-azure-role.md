---
id: cloud-azure-role
title: Azure identity is a role assignment graph
tags: cloud, azure, iam
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Azure identity is a role assignment graph

## Claim

A managed identity, service principal or guest has a role at a scope that reaches a subscription or a key vault.

## Test

List role assignments for the identity. Check scope inheritance. Test a read at the highest scope.

## Proof

A read of a resource outside the intended scope.

## Failure modes

A role definition name is not the effective permission. Conditions and PIM change it.
