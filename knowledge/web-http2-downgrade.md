---
id: web-http2-downgrade
title: HTTP/2 adds a second parser for the same request
tags: web, http2, smuggling
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# HTTP/2 adds a second parser for the same request

## Claim

Pseudo-headers, header casing, HPACK and a downgrade to HTTP/1.1 can create a disagreement between front and back ends.

## Test

Send duplicate or malformed pseudo-headers. Test header names with spaces and connection-specific headers. Compare with an HTTP/1.1 client.

## Proof

A desync, a request split, or a response for another user.

## Failure modes

A 400 from the edge does not prove safety. Not every proxy downgrades.
