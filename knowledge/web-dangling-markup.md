---
id: web-dangling-markup
title: Dangling markup leaks what follows the injection
tags: web, html, csrf
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# Dangling markup leaks what follows the injection

## Claim

An unclosed attribute or tag makes the parser swallow later markup, including a CSRF token, into a URL.

## Test

Inject an unterminated img or form tag. Watch the listener for the swallowed page content.

## Proof

A request that carries the token from later in the page.

## Failure modes

A page with no secret after the sink gives little. CSP can block the request.
