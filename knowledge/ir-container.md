---
id: ir-container
title: Container triage is image diff plus runtime state
tags: ir, container, docker
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Container triage is image diff plus runtime state

## Claim

The running container may differ from the image, and the host sees the process and mounts.

## Test

Diff the container filesystem against the image. Check processes, mounts and network. Inspect the host.

## Proof

A file or process not present in the image.

## Failure modes

A writable layer is expected for logs. A changed binary is not.
