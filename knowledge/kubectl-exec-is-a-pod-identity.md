---
id: kubectl-exec-is-a-pod-identity
title: kubectl exec is a pod identity
tags: k8s, exec, rbac
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# kubectl exec is a pod identity

## Claim

The pods/exec subresource lets a user run a shell in a pod with the pod service account and mounted secrets.

## Test

Check the exec right. Run a shell in a chosen pod. Read the token and the mounts.

## Proof

A shell and a service account token.

## Failure modes

A limited pod with no token or mount has low value. A read only exec can be enough to read.
