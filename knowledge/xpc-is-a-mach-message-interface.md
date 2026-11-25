---
id: xpc-is-a-mach-message-interface
title: XPC is a mach message interface
tags: macos, xpc, ipc
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# XPC is a mach message interface

## Claim

An XPC service receives a dictionary from a client. A missing audit token or type check lets another app call it.

## Test

List the services and the plist. Read the handler. Connect with a small client and send a malformed dictionary.

## Proof

A privileged action from a client the service did not expect.

## Failure modes

A code signing requirement on the peer closes it. A sandboxed client can still reach the service.
