---
id: web-cache-deception
title: Cache deception dresses a private page as a static file
tags: web, cache, deception
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Cache deception dresses a private page as a static file

## Claim

The cache stores an authenticated response because the path looks static, then serves it to an unauthenticated user. Poisoning changes the content; deception leaks it.

## Test

Request /account with a static-looking suffix such as /account.css or /account/%2e.css. Request the same URL without cookies. Compare.

## Proof

An unauthenticated request returns the victim's private page from cache.

## Failure modes

A cache hit for your own cookie is not global. The origin must return the private content for the disguised path.
