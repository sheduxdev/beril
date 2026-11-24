---
id: firmware-spi
title: SPI flash reads need two matching dumps
tags: firmware, hardware, spi
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/firmware-iot.md
status: active
---
# SPI flash reads need two matching dumps

## Claim

The firmware lives on an SPI NOR chip. A bad clip or voltage gives a corrupt image.

## Test

Use a SOIC clip and a programmer. Read twice and compare hashes. Identify the chip before writing.

## Proof

Two identical dumps and a mounted filesystem.

## Failure modes

A single read can look valid and still be corrupt. Do not write without a backup.
