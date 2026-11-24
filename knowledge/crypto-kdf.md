---
id: crypto-kdf
title: A password hash is a cost parameter
tags: crypto, kdf, password
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/vulnerability-research.md
status: active
---
# A password hash is a cost parameter

## Claim

Argon2, scrypt, bcrypt or PBKDF2 with a low cost or a shared salt makes cracking cheaper.

## Test

Read the algorithm and parameters. Check the salt uniqueness. Estimate the crack cost.

## Proof

A parameter set below current guidance or a reused salt.

## Failure modes

A fast hash can be acceptable for a high-entropy token. A password needs a slow KDF.
