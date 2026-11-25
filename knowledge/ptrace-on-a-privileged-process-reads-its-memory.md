---
id: ptrace-on-a-privileged-process-reads-its-memory
title: ptrace on a privileged process reads its memory
tags: linux, ptrace, memory
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# ptrace on a privileged process reads its memory

## Claim

The ptrace scope and the Yama setting decide whether a user can attach to a process and read its secrets.

## Test

Read `/proc/sys/kernel/yama/ptrace_scope`. Attach to a target with gdb or a small tracer. Read the heap.

## Proof

A secret from the process memory.

## Failure modes

Scope 1 limits to children. A process can drop privileges before the attach.
