---
id: a-key-in-the-client-is-a-public-key-not-a-secret
title: A key in the client is a public key, not a secret
tags: crypto, key, client
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A key in the client is a public key, not a secret

## Claim

A signing or encryption key shipped in JavaScript or an app bundle can only protect against users who do not open the bundle.

## Test

Extract the key from the bundle. Resign or decrypt a request with it.

## Proof

The forged request is accepted.

## Failure modes

Server side key binding or a second secret can raise the bar. Obfuscation alone does not.
