---
id: adfs-metadata-is-a-trust-document
title: ADFS metadata is a trust document
tags: idp, adfs, saml
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-saml-signature-wrapping.md
status: active
---
# ADFS metadata is a trust document

## Claim

The federation metadata publishes the signing certificate, the endpoints and the entity id. A trust that refreshes it accepts a new key.

## Test

Read the metadata and the trust. Check the certificate and the refresh. Compare the entity id.

## Proof

A trust change from a metadata refresh.

## Failure modes

A manual certificate pin blocks it. A short validity can hide the change.
