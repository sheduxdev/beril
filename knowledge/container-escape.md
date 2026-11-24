---
id: container-escape
title: A container escape is a host resource exposed to the container
tags: container, escape, kubernetes
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# A container escape is a host resource exposed to the container

## Claim

The container has a host mount, the runtime socket, privileged devices or a kernel bug surface.

## Test

List mounts, capabilities, devices and namespaces. Try a host read through each. Check the kernel version.

## Proof

A host file read, a host process signal, or a new container with host mounts.

## Failure modes

Root inside a container is not root on the host by itself. User namespaces change the mapping.
