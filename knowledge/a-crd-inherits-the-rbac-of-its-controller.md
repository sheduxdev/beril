---
id: a-crd-inherits-the-rbac-of-its-controller
title: A CRD inherits the RBAC of its controller
tags: k8s, crd, rbac
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# A CRD inherits the RBAC of its controller

## Claim

A custom resource can make the controller act on a cluster resource with the controller role, even when the user has no direct right.

## Test

Read the CRD schema and the controller role. Create a resource that names a target. Watch the controller action.

## Proof

An action outside the user RBAC through the CRD.

## Failure modes

A validating webhook can restrict the fields. A namespaced controller limits the scope.
