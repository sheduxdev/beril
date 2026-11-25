---
id: a-secure-boot-fuse-is-one-way
title: A secure boot fuse is one way
tags: hardware, secure-boot, fuse
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-secureboot.md
status: active
---
# A secure boot fuse is one way

## Claim

Burning the key hash fuse makes the ROM accept only signed images. The burn cannot be undone.

## Test

Read the fuse map and the boot log. Confirm the key hash slot. Try an unsigned image before and after.

## Proof

A rejected unsigned image with the fuse set.

## Failure modes

A development unit ships unblown. A recovery mode can still allow a signed image only.
