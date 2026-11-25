---
id: an-azure-role-assignment-is-the-effective-right
title: An Azure role assignment is the effective right
tags: azure, role, rbac
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-azure-role.md
status: active
---
# An Azure role assignment is the effective right

## Claim

Azure RBAC is additive. A role at a management group or subscription reaches every resource below it.

## Test

List the assignments at each scope. Expand the inherited ones. Map the actions in the role definition.

## Proof

A read or write on a target below the inherited scope.

## Failure modes

A deny assignment or a PIM activation blocks it. A narrow custom role limits the actions.
