---
id: an-ecu-is-a-computer-with-a-bootloader
title: An ECU is a computer with a bootloader
tags: auto, ecu, bootloader
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-update-sign.md
status: active
---
# An ECU is a computer with a bootloader

## Claim

The ECU has a bootloader and a flash. A diagnostic session can enter it and accept an image.

## Test

Read the ECU part and the diagnostic services. Enter the programming session. Read the flash id.

## Proof

A bootloader session and a flash id.

## Failure modes

A signed image requirement blocks a custom flash. A gateway can limit the session.
