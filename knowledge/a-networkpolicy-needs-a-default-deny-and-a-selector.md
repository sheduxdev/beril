---
id: a-networkpolicy-needs-a-default-deny-and-a-selector
title: A NetworkPolicy needs a default deny and a selector
tags: k8s, networkpolicy, segmentation
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-service-mesh.md
status: active
---
# A NetworkPolicy needs a default deny and a selector

## Claim

A policy that selects no pods or only allows egress does not create a default deny. The namespace stays flat.

## Test

List the policies. Check the pod selector and the policy types. Connect from an unselected pod.

## Proof

A connection that the policy should block.

## Failure modes

A CNI can add a default deny. A policy on all pods closes it.
