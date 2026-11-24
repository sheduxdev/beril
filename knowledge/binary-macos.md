---
id: binary-macos
title: Mach-O and dyld define what loads before main
tags: binary, macos, macho
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/reverse-engineering.md
status: active
---
# Mach-O and dyld define what loads before main

## Claim

Load commands, LC_LOAD_DYLIB, rpaths and entitlements decide which code runs and what it may do.

## Test

List load commands, libraries and rpaths. Check the signature and entitlements. Try a dylib hijack in a lab.

## Proof

A loaded library or entitlement that changes behavior.

## Failure modes

Hardened runtime and library validation block some hijacks. A signed app is not automatically safe.
