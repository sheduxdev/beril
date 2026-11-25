---
id: code-signing-is-a-chain-and-an-entitlement-set
title: Code signing is a chain and an entitlement set
tags: macos, codesign, entitlement
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Code signing is a chain and an entitlement set

## Claim

The signature binds the binary to an identity and the entitlements grant rights. A mismatched entitlement is a boundary bug.

## Test

Run `codesign -dvvv` and `--entitlements`. Compare the set with the behavior. Check the team id and the hardened runtime.

## Proof

An entitlement used by the app to cross a right it should not hold.

## Failure modes

A library validation flag can block injection. A revoked certificate breaks the app.
