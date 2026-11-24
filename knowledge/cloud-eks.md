---
id: cloud-eks
title: EKS has two identity planes: IAM and Kubernetes
tags: cloud, eks, kubernetes
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# EKS has two identity planes: IAM and Kubernetes

## Claim

aws-auth maps IAM roles to Kubernetes groups, and IRSA lets a pod assume an IAM role. A mismatch crosses the boundary.

## Test

Read aws-auth and service account annotations. Test the pod identity with aws sts. Test the Kubernetes RBAC.

## Proof

An IAM or Kubernetes action the pod's role should not have.

## Failure modes

A node role is shared by all pods on the node. IRSA is narrower.
