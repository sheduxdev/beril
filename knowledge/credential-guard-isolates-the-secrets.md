---
id: credential-guard-isolates-the-secrets
title: Credential Guard isolates the secrets
tags: wink, credential-guard, lsass
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/win-credential-stores.md
status: active
---
# Credential Guard isolates the secrets

## Claim

The LSA secrets live in a VBS process. A plain LSASS dump can miss the derived credentials.

## Test

Read the VBS state. Dump LSASS. Compare the secrets with a Guard off host.

## Proof

A missing credential in the dump.

## Failure modes

A Guard off host has everything. A signed driver can still read the VBS memory.
