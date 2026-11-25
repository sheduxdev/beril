---
id: kernel-modprobe-path-is-a-write-target
title: Kernel modprobe_path is a write target
tags: pwn, kernel, modprobe
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/binary-kernel.md
status: active
---
# Kernel modprobe_path is a write target

## Claim

The kernel runs `modprobe_path` when it meets an unknown binary format. A write to that global gives root code execution.

## Test

Find the symbol address. Write a script path. Execute a file with an unknown magic.

## Proof

The script runs as root.

## Failure modes

A read only global or a namespaced kernel blocks it. A container can share the host path.
