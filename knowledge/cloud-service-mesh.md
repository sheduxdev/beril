---
id: cloud-service-mesh
title: A sidecar is a second network path
tags: cloud, istio, mtls
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/vulnerability-research.md
status: active
---
# A sidecar is a second network path

## Claim

mTLS proves the workload, but AuthorizationPolicy decides the call. A permissive policy or a direct pod path bypasses the mesh.

## Test

Read the policy. Call through the mesh and directly to the pod IP. Check the identity header.

## Proof

A direct call that should have been denied.

## Failure modes

A deny-all default is the safe base. A port-forward is not a bypass.
