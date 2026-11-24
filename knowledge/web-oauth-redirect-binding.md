---
id: web-oauth-redirect-binding
title: OAuth redirect matching is prefix logic under pressure
tags: web, oauth, identity
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/claude-bughunter.md
status: active
---
# OAuth redirect matching is prefix logic under pressure

## Claim

The authorization server compares redirect URIs with loose rules. Path traversal, a subdomain, an open redirect or a fragment can move the code.

## Test

Map every redirect URI and the matching rule. Test path, query, fragment, subdomain, case and open redirect on an allowed host. Reuse state and nonce.

## Proof

A code or token delivered to an attacker-controlled origin, then exchanged for a session.

## Failure modes

A login CSRF needs a victim action. A code for your own account is not account takeover.
