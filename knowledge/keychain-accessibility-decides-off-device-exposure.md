---
id: keychain-accessibility-decides-off-device-exposure
title: Keychain accessibility decides off device exposure
tags: mobile, ios, keychain
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Keychain accessibility decides off device exposure

## Claim

`kSecAttrAccessibleAlways` keeps the item readable on a locked device and in a backup, unlike WhenUnlockedThisDeviceOnly.

## Test

Read the protection class in the binary or a hook. Lock the device and read the item with a script.

## Proof

The secret is read while locked or restored to another device.

## Failure modes

A background refresh need can justify Always. A this device only class blocks restore.
