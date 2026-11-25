---
id: a-loader-is-a-small-stage-and-a-decoder
title: A loader is a small stage and a decoder
tags: malware, loader, stage
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mal-process-injection.md
status: active
---
# A loader is a small stage and a decoder

## Claim

The first stage allocates, decodes and jumps. The real payload is in memory, so a disk scan misses it.

## Test

Debug the loader. Break after the allocation and the decode. Dump the region before the jump.

## Proof

A dumped stage with the decoded header.

## Failure modes

A staged loader can sleep and check the debugger. A process hollowing target needs the target dump.
