---
id: web-open-redirect-chain
title: Open redirect matters when a token rides the URL
tags: web, redirect, oauth
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Open redirect matters when a token rides the URL

## Claim

A redirect parameter accepts an absolute or scheme-relative URL, and an auth flow returns a code or token to it.

## Test

Test absolute, //host, backslash, encoded and userinfo forms. Put the redirect in an OAuth flow.

## Proof

A code or token delivered to an attacker origin.

## Failure modes

A redirect to the same host is not open. A 302 without a token can still be low.
