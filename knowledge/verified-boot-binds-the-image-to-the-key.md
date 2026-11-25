---
id: verified-boot-binds-the-image-to-the-key
title: Verified boot binds the image to the key
tags: android, verified-boot, boot
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-secureboot.md
status: active
---
# Verified boot binds the image to the key

## Claim

The boot chain checks the vbmeta signature and the hash tree. A custom image needs a key and a disabled verification or a signed vbmeta.

## Test

Read the boot state and the vbmeta. Flash a test image with verification on and off. Compare the state.

## Proof

A boot refusal with verification on.

## Failure modes

A user can disable verification on an unlocked bootloader. A locked device needs a signed image.
