---
id: win-credential-stores
title: Windows keeps credentials in more than one place
tags: windows, credentials, dpapi
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Windows keeps credentials in more than one place

## Claim

DPAPI blobs, Credential Manager, browser stores and Wi-Fi profiles hold secrets tied to the user or machine.

## Test

Enumerate vaults and DPAPI blobs. Decrypt with the user context or the backup key. Check browser stores.

## Proof

A recovered credential used for a new access.

## Failure modes

A blob without the master key is not readable. Machine and user scopes differ.
