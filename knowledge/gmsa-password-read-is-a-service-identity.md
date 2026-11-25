---
id: gmsa-password-read-is-a-service-identity
title: gMSA password read is a service identity
tags: win, gmsa, password
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# gMSA password read is a service identity

## Claim

Read access to the managed password attribute gives the service account hash, which is usable without cracking.

## Test

Check the read right on the gMSA object. Read `msDS-ManagedPassword`. Convert the blob to an NT hash.

## Proof

A session or a pass the hash as the service.

## Failure modes

A gMSA with a limited logon scope restricts where the hash works. The read right can be rare.
