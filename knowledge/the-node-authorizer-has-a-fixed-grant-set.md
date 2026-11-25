---
id: the-node-authorizer-has-a-fixed-grant-set
title: The node authorizer has a fixed grant set
tags: k8s, node, authorizer
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# The node authorizer has a fixed grant set

## Claim

A kubelet identity can read the pods, secrets and configmaps assigned to its node, and a compromised node reaches them.

## Test

Check the node identity and the assigned pods. Read a secret for a pod on the node. Try another node's pod.

## Proof

A secret for a pod outside your namespace.

## Failure modes

A node with few pods limits the reach. The authorizer can be disabled.
