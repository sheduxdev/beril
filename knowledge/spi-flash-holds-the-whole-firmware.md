---
id: spi-flash-holds-the-whole-firmware
title: SPI flash holds the whole firmware
tags: firmware, spi, dump
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-spi.md
status: active
---
# SPI flash holds the whole firmware

## Claim

An in circuit SPI dump can recover the rootfs, keys and the update logic without desoldering.

## Test

Identify the chip and the pinout. Clip with the power off or hold the CPU in reset. Read with flashrom and verify twice.

## Proof

Two matching dumps with a known filesystem inside.

## Failure modes

A clip can shift. A read protection bit blocks it.
