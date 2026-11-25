---
id: spi-flash-holds-the-boot-image-and-the-keys
title: SPI flash holds the boot image and the keys
tags: hardware, spi, flash
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-spi.md
status: active
---
# SPI flash holds the boot image and the keys

## Claim

The boot flash is readable with a clip when the CPU is held in reset. It holds the rootfs, the update key and the device identity.

## Test

Identify the chip. Clip with power off or reset held. Read twice with flashrom and compare.

## Proof

Two matching dumps and a filesystem or a key inside.

## Failure modes

A read protection bit blocks it. A clip can shift on a fine pitch.
