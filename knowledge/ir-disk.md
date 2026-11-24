---
id: ir-disk
title: Disk artifacts answer who, what and when
tags: ir, disk, forensics
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Disk artifacts answer who, what and when

## Claim

MFT, USN, registry, prefetch and event logs reconstruct execution and persistence.

## Test

Collect the artifacts. Normalize timestamps. Correlate a binary path with execution and network.

## Proof

A timeline with a binary, a user and a connection.

## Failure modes

A timestamp can be modified. Prefetch can be disabled.
