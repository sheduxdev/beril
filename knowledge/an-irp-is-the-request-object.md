---
id: an-irp-is-the-request-object
title: An IRP is the request object
tags: wink, irp, driver
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/binary-windows-kernel.md
status: active
---
# An IRP is the request object

## Claim

The IRP carries the buffer, the length and the major function. A handler that trusts the IRP fields without a probe reads user memory as kernel.

## Test

Read the dispatch table. Send a crafted IRP through the device. Watch the access and the completion.

## Proof

A kernel read from a user address or a crash.

## Failure modes

A buffered IO flag copies first. A filter driver can change the IRP.
