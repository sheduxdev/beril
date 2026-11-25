---
id: dpapi-master-keys-follow-the-user
title: DPAPI master keys follow the user
tags: win, dpapi, credential
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/win-credential-stores.md
status: active
---
# DPAPI master keys follow the user

## Claim

A user master key decrypts every DPAPI blob for that user, so the key plus the blob plus the password or domain backup is the secret.

## Test

Find the master key and the blob. Check the protection. Decrypt with the user context or the domain backup key.

## Proof

A plaintext credential or token.

## Failure modes

A domain backup key needs domain admin. A roaming profile moves the key.
