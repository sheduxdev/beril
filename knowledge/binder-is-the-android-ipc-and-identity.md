---
id: binder-is-the-android-ipc-and-identity
title: Binder is the Android IPC and identity
tags: android, binder, ipc
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mobile-deep-link-bridge.md
status: active
---
# Binder is the Android IPC and identity

## Claim

Every Binder call carries a uid and a pid. A service that trusts the caller without checking the uid is open to any app.

## Test

List the services and the transactions. Connect with a helper app. Send a call with a spoofed package or a missing check.

## Proof

A privileged action from the helper app.

## Failure modes

A signature permission closes it. A service can run in the same process as the caller.
