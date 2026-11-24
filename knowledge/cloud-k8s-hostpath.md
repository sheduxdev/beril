---
id: cloud-k8s-hostpath
title: A privileged pod with hostPath is a host escape
tags: cloud, kubernetes, container
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/cloud
status: active
---
# A privileged pod with hostPath is a host escape

## Claim

The pod runs privileged or as root and mounts a sensitive host path. The container can read or write host state.

## Test

Read /host/etc/shadow. Check the service account token. Look for the runtime socket.

## Proof

A host file or token read from inside the pod.

## Failure modes

hostPath alone without privilege is weaker. A read-only mount limits writes.
