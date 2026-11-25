---
id: fsop-targets-the-file-vtable-and-the-lock
title: FSOP targets the FILE vtable and the lock
tags: pwn, fsop, libc
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# FSOP targets the FILE vtable and the lock

## Claim

A forged FILE structure can call a vtable function during flush, close or exit, which is a libc only control path.

## Test

Place a fake FILE in known memory. Set the vtable and the wide data. Trigger fclose or exit.

## Proof

The chosen function is called with the FILE pointer.

## Failure modes

A vtable check in newer glibc requires a valid section address. A known libc is needed.
