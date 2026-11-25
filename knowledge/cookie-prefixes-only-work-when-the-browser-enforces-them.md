---
id: cookie-prefixes-only-work-when-the-browser-enforces-them
title: Cookie prefixes only work when the browser enforces them
tags: auth, cookie, session
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-csrf-samesite.md
status: active
---
# Cookie prefixes only work when the browser enforces them

## Claim

__Host requires Secure, Path=/ and no Domain. A cookie set without those attributes is rejected or can be shadowed by a sibling subdomain.

## Test

Try to set __Host-session from a subdomain and from HTTP. Compare which cookie the app reads.

## Proof

A shadow cookie changes the authenticated state.

## Failure modes

Some old clients ignore prefixes. A proxy that rewrites cookies hides the issue.
