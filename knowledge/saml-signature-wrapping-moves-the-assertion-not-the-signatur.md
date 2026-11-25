---
id: saml-signature-wrapping-moves-the-assertion-not-the-signatur
title: SAML signature wrapping moves the assertion, not the signature
tags: auth, saml, xsw
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-saml-signature-wrapping.md
status: active
---
# SAML signature wrapping moves the assertion, not the signature

## Claim

A valid signed assertion can be kept while a second assertion with attacker claims is placed where the parser reads it.

## Test

Capture a signed response. Duplicate the assertion, change the first subject or attributes, keep the signature reference valid.

## Proof

The SP logs in as the altered subject.

## Failure modes

A strict parser that selects the signed assertion by ID resists the basic wrap. Namespace and ID changes need care.
