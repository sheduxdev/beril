---
id: webauthn-trusts-the-rp-id-and-origin-pair
title: WebAuthn trusts the RP ID and origin pair
tags: auth, passkey, webauthn
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# WebAuthn trusts the RP ID and origin pair

## Claim

A server that accepts an origin it does not own, or derives the RP ID from the request, can accept a credential from another site.

## Test

Register a credential for a related origin, then log in through the target. Compare the RP ID in the client data.

## Proof

A credential from the other origin is accepted.

## Failure modes

Browser checks are strict. A subdomain RP ID can be valid by design.
