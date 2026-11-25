---
id: a-cache-that-ignores-the-user-cookie-leaks-across-accounts
title: A cache that ignores the user cookie leaks across accounts
tags: web, cache, session
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-cache-key-unkeyed-input.md
status: active
---
# A cache that ignores the user cookie leaks across accounts

## Claim

If the cache key omits the session or a user varying cookie, the first authenticated response is served to the next visitor.

## Test

Request an account page as user A. Request it without cookies and as user B. Compare the body and the cache headers.

## Proof

User B receives user A content from the cache.

## Failure modes

A private cache directive prevents it. A CDN rule can strip the cookie before the key.
