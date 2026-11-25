---
id: an-entitlement-is-the-macos-capability
title: An entitlement is the macOS capability
tags: macos, entitlement, capability
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# An entitlement is the macOS capability

## Claim

`com.apple.security.cs.allow-jit`, `disable-library-validation` and the sandbox entitlements each open a specific path.

## Test

List the entitlements on the app and its helpers. Map each to a capability. Test the one with the most reach.

## Proof

A behavior that depends on the entitlement.

## Failure modes

A hardened runtime can still restrict it. A helper can hold the right instead.
