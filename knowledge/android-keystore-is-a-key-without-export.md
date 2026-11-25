---
id: android-keystore-is-a-key-without-export
title: Android Keystore is a key without export
tags: android, keystore, key
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Android Keystore is a key without export

## Claim

A keystore key performs the operation in the TEE or StrongBox and the private key does not leave. The auth binding is the control.

## Test

Read the key generation. Check the user auth and the invalidate flags. Try the operation locked and unlocked.

## Proof

A key failure under the wrong auth state.

## Failure modes

A software backed key can be extracted on a rooted device. A StrongBox key has a separate limit.
