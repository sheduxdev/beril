---
id: an-i2c-eeprom-is-a-small-config-store
title: An I2C EEPROM is a small config store
tags: hardware, i2c, eeprom
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-spi.md
status: active
---
# An I2C EEPROM is a small config store

## Claim

A serial EEPROM on the bus often holds the MAC, the calibration or the feature flags, and it is readable with a cheap adapter.

## Test

Scan the bus for addresses. Read the first page. Compare two devices. Change one byte and watch the boot.

## Proof

A config change that survives a reboot.

## Failure modes

A write protect pin blocks the write. The address can collide with a sensor.
