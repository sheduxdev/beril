---
id: rbac-bind-and-escalate-are-the-quiet-paths
title: RBAC bind and escalate are the quiet paths
tags: cloud, k8s, rbac
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# RBAC bind and escalate are the quiet paths

## Claim

The `bind` and `escalate` verbs let a role create a stronger binding without holding the stronger permissions.

## Test

Check the role rules for bind or escalate. Create a RoleBinding to cluster-admin or to a powerful built in role.

## Proof

The new binding grants the higher role.

## Failure modes

A namespace scoped binding still only affects that namespace. Aggregation can hide the right.
