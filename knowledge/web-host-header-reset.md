---
id: web-host-header-reset
title: Password reset trusts the request host
tags: web, host-header, email
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Password reset trusts the request host

## Claim

The reset link is built from Host, X-Forwarded-Host or Forwarded without an allowlist.

## Test

Request a reset with each header set to a controlled domain. Check the email and exchange the token.

## Proof

A reset link on the attacker host with a valid token.

## Failure modes

A reflected host in the page is not the same as a host used in email. Proxies normalize.
