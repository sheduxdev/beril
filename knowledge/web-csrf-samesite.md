---
id: web-csrf-samesite
title: CSRF survives when state changes on a safe method
tags: web, csrf, session
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# CSRF survives when state changes on a safe method

## Claim

A state change is reachable by GET, or SameSite is absent and the token is not bound to the session. JSON content type alone is not a defense.

## Test

Map state-changing GETs. Check SameSite, Origin and Referer checks. Replay the request from a cross-site page.

## Proof

A victim session performs the change without seeing the response.

## Failure modes

A missing token with SameSite=Lax can still be safe for POST. Login CSRF is a separate impact.
