---
id: port-forward-bypasses-the-ingress-path
title: Port forward bypasses the ingress path
tags: k8s, portforward, rbac
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# Port forward bypasses the ingress path

## Claim

The pods/portforward right opens a local port to a pod without an ingress, a service or an auth proxy.

## Test

Check the right. Forward a pod port. Call the app on localhost and compare with the public URL.

## Proof

A backend response on the local port.

## Failure modes

A pod that binds loopback only needs a different port. A network policy can still block.
