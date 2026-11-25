---
id: a-browser-sandbox-escape-is-a-broker-message-bug
title: A browser sandbox escape is a broker message bug
tags: browser, sandbox, ipc
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-browser.md
status: active
---
# A browser sandbox escape is a broker message bug

## Claim

The renderer talks to a privileged broker through an IPC surface. A confused message or a type mix up crosses the boundary.

## Test

List the exposed interfaces and the message types. Send malformed fields. Watch the broker process and the file access.

## Proof

A privileged action from a compromised renderer.

## Failure modes

A strict mojo or IPC validator blocks it. A renderer already in the sandbox still needs a broker bug.
