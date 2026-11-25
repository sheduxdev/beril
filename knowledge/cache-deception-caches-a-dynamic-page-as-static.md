---
id: cache-deception-caches-a-dynamic-page-as-static
title: Cache deception caches a dynamic page as static
tags: web, cache, deception
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-cache-deception.md
status: active
---
# Cache deception caches a dynamic page as static

## Claim

A path like /account.css on a framework that ignores the extension can be cached as a static asset and served to others.

## Test

Request /account, then /account.css, then /account without cookies. Compare which response is cached.

## Proof

The authenticated body is returned from the cache to a cookieless request.

## Failure modes

The server can normalize the path and return 404. A cache bypass header blocks it.
