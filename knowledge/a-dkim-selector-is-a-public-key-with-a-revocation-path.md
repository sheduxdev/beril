---
id: a-dkim-selector-is-a-public-key-with-a-revocation-path
title: A DKIM selector is a public key with a revocation path
tags: mail, dkim, selector
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/email-dkim.md
status: active
---
# A DKIM selector is a public key with a revocation path

## Claim

The selector under `_domainkey` publishes the key. A short key or a leaked private key allows signing as the domain.

## Test

Enumerate common selectors. Read the key type and length. Sign a message with a test key and check the pass.

## Proof

A valid signature from a key you control.

## Failure modes

A 2048 bit key with a protected private key holds. An unused selector can stay published.
