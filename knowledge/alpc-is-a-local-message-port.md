---
id: alpc-is-a-local-message-port
title: ALPC is a local message port
tags: wink, alpc, ipc
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# ALPC is a local message port

## Claim

An ALPC port carries messages and handles between processes. A missing sender check or a handle type mix up crosses the boundary.

## Test

List the ports and the owners. Read the message handler. Send a crafted message from a helper process.

## Proof

A privileged action or a handle leak.

## Failure modes

A port with a security descriptor can restrict the sender. A message can be validated by the server.
