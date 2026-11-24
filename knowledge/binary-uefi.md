---
id: binary-uefi
title: UEFI is an event-driven firmware runtime
tags: binary, uefi, firmware
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/reverse-engineering.md
status: active
---
# UEFI is an event-driven firmware runtime

## Claim

DXE drivers, protocols and SMM handlers parse variables and capsules with limited validation.

## Test

Extract the firmware. Map DXE and SMM. Check variable parsing and capsule updates. Emulate with QEMU or a lab.

## Proof

A controlled write or a secure boot bypass.

## Failure modes

A DXE driver that never runs is dead code. SMM needs a special entry.
