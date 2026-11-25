---
id: the-keyring-is-a-per-user-secret-store
title: The keyring is a per user secret store
tags: link, keyring, secret
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/linux-keyring.md
status: active
---
# The keyring is a per user secret store

## Claim

Keys are linked to a process keyring and inherited. A readable keyring is a credential without a file.

## Test

List the keyrings and the permissions. Read a key with `keyctl`. Compare with the process user.

## Proof

A key value from another process.

## Failure modes

A session keyring can be isolated. A key can be revoked early.
