---
id: web-saml-signature-wrapping
title: SAML trusts the assertion, not the signature
tags: web, saml, identity
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/experts.md
status: active
---
# SAML trusts the assertion, not the signature

## Claim

The service provider reads an assertion that the signature does not cover, or resolves an ID to a different node than the signer.

## Test

Capture a valid response. Move or duplicate the signed assertion. Change unsigned identity fields and test attribute pollution.

## Proof

A fresh session as the target user from a response signed for another.

## Failure modes

A decoded assertion is not a bypass. XML canonicalization changes can break the test.
