---
id: saml-metadata-can-carry-a-redirect-and-a-key
title: SAML metadata can carry a redirect and a key
tags: idp, saml, metadata
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-saml-signature-wrapping.md
status: active
---
# SAML metadata can carry a redirect and a key

## Claim

The metadata contains the SSO URL and the signing certificate. A trust that imports it follows both.

## Test

Read the metadata. Compare the URL and the key with the trust. Change one in a test trust.

## Proof

A login redirect to the changed URL.

## Failure modes

A pinned URL blocks it. A metadata refresh can need an admin.
