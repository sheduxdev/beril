---
id: kernel-cred-overwrite-is-the-shortest-root
title: Kernel cred overwrite is the shortest root
tags: pwn, kernel, cred
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-kernel.md
status: active
---
# Kernel cred overwrite is the shortest root

## Claim

A task struct holds the credential pointer. Overwriting the uid fields or the pointer to a prepared cred gives root.

## Test

Find the current task. Locate cred. Write zero to the uid fields or swap the pointer.

## Proof

The process reads files as root.

## Failure modes

A namespace uid mapping or a hardened cred check blocks it. SMAP needs a kernel copy.
