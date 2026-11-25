---
id: isolation-needs-a-kernel-or-a-hardware-boundary
title: Isolation needs a kernel or a hardware boundary
tags: design, isolation, sandbox
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/os-namespaces.md, knowledge/cloud-k8s-hostpath.md
status: active
---
# Isolation needs a kernel or a hardware boundary

## Claim

A namespace, a container and a VM are different strengths. A shared kernel is not a security boundary against a kernel bug.

## Test

Read the isolation layer. Check the seccomp, the user namespace and the device access. Find one shared resource.

## Proof

A shared resource reachable across the boundary.

## Failure modes

A hardened runtime adds a layer. A single tenant host needs less isolation.
