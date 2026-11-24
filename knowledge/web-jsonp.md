---
id: web-jsonp
title: JSONP is script injection with a callback name
tags: web, jsonp, script
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# JSONP is script injection with a callback name

## Claim

The endpoint reflects a callback parameter into a JavaScript response with the wrong content type.

## Test

Send callback=alert(1) variants. Check the content type and the wrapper. Load it as a script from another origin.

## Proof

A function call or expression executes in the page.

## Failure modes

A fixed callback is not injectable. A JSON content type with nosniff may block it.
