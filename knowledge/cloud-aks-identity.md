---
id: cloud-aks-identity
title: AKS mixes Azure RBAC and Kubernetes RBAC
tags: cloud, aks, kubernetes
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# AKS mixes Azure RBAC and Kubernetes RBAC

## Claim

Workload identity federates a service account to Azure, and Azure RBAC controls the cluster. A role at the wrong scope crosses tenants.

## Test

Read the federated credential and role assignment. Test the pod token against Azure and the K8s API.

## Proof

An Azure or K8s action outside the intended scope.

## Failure modes

A cluster-admin binding is obvious. A custom role with wildcard verbs is not.
