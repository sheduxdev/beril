---
id: web-client-path-traversal
title: Client-side path traversal is a router normalization bug
tags: web, spa, router
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Client-side path traversal is a router normalization bug

## Claim

A file or route parameter accepts ../ and the client fetches a path outside its base.

## Test

Try ../, encoded, and double-encoded values in route and file parameters. Watch the network path.

## Proof

A fetch for a path outside the intended directory.

## Failure modes

A server-side 404 can hide a client-side fetch that already happened. Check the request.
