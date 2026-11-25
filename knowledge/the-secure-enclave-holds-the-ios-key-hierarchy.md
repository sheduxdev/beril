---
id: the-secure-enclave-holds-the-ios-key-hierarchy
title: The Secure Enclave holds the iOS key hierarchy
tags: ios, secure-enclave, key
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# The Secure Enclave holds the iOS key hierarchy

## Claim

The SEP holds the class keys and the passcode binding. A key with a WhenPasscodeSet class is unavailable without the passcode.

## Test

Read the protection class on the key. Lock the device. Try to use the key with and without the passcode.

## Proof

A key failure while the device is locked.

## Failure modes

A background entitlement can keep a key available. A jailbroken device changes the model.
