---
id: auth-phishing-resistant
title: Phishing-resistant MFA binds the credential to the origin
tags: auth, fido2, webauthn, phishing
confidence: high
updated: 2026-11-26
uses: 0
sources: https://www.cisa.gov/resources-tools/resources/implementing-phishing-resistant-mfa, https://fidoalliance.org/specifications/, https://www.w3.org/TR/webauthn-2/
status: active
---
# Phishing-resistant MFA binds the credential to the origin

## Claim

FIDO2 or WebAuthn and PKI smart cards sign a challenge with a private key tied to the real origin, so a proxy phishing page or a relay cannot replay it. CISA calls this the gold standard.

## Test

Enroll a passkey or security key. Try to authenticate through an attacker-in-the-middle proxy that serves a look-alike origin. The key should refuse because the origin does not match.

## Proof

An authentication that fails on the wrong origin and succeeds only on the registered one, with no shared code to steal.

## Failure modes

A fallback to OTP or push reopens the hole; account recovery is the new weakest link. Transition-mode or hybrid rollouts leave a phishable path until the fallback is removed.
