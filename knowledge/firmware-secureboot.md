---
id: firmware-secureboot
title: Secure boot is a chain, not a boolean
tags: firmware, secureboot, boot
confidence: high
updated: 2026-11-24
uses: 0
sources: references/firmware-iot.md
status: active
---
# Secure boot is a chain, not a boolean

## Claim

Each stage verifies the next with a key from a trusted store. One unsigned stage or a writable key store breaks the chain.

## Test

Map ROM, bootloader, kernel and rootfs. Check each signature and key. Try a modified stage.

## Proof

A modified stage that still boots.

## Failure modes

A lock stated in config may not be enforced. Recovery mode can bypass.
