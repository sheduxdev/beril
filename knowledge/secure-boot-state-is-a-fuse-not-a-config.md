---
id: secure-boot-state-is-a-fuse-not-a-config
title: Secure boot state is a fuse, not a config
tags: firmware, secureboot, fuse
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-secureboot.md
status: active
---
# Secure boot state is a fuse, not a config

## Claim

The boot ROM reads the fuse state before any image. Once the fuse is burned, a signed image is the only path.

## Test

Read the fuse map and the boot log. Check whether the key hash is programmed. Try an unsigned image.

## Proof

The unsigned image is rejected and the fuse bit is set.

## Failure modes

A development board ships unblown. A recovery mode can still accept a signed image only.
