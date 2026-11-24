---
id: ir-memory
title: Memory is the most volatile evidence
tags: ir, memory, forensics
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Memory is the most volatile evidence

## Claim

Running processes, keys and network state disappear on shutdown. Capture memory before disk if the system is live.

## Test

Record the order. Capture memory with a known tool. Hash it. Capture disk after.

## Proof

A memory image with a hash and a process list that matches the host.

## Failure modes

A memory image from a different build is hard to symbolize. Do not reboot first.
