---
id: postmessage-needs-origin-and-source-checks
title: postMessage needs origin and source checks
tags: browser, postmessage, origin
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-postmessage.md
status: active
---
# postMessage needs origin and source checks

## Claim

A listener that trusts `event.data` without checking `event.origin` or `event.source` accepts messages from any frame.

## Test

Read every listener. Open the page in an iframe you control. Send the expected message shape from the parent.

## Proof

The target performs the action or returns data to the wrong frame.

## Failure modes

An origin allowlist and a source check close it. A wildcard targetOrigin only affects the reply.
