---
id: pkce-can-be-stripped-when-the-server-does-not-require-it
title: PKCE can be stripped when the server does not require it
tags: auth, oauth, pkce
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# PKCE can be stripped when the server does not require it

## Claim

If the authorization server accepts a public client without code_challenge, an attacker who steals the code can redeem it.

## Test

Start a flow with PKCE, remove code_challenge from the authorize request, keep the verifier out of the token call.

## Proof

The token endpoint returns tokens without a verifier.

## Failure modes

Confidential clients with a secret are less exposed. A strict server rejects the downgrade.
