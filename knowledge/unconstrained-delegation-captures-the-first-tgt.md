---
id: unconstrained-delegation-captures-the-first-tgt
title: Unconstrained delegation captures the first TGT
tags: ad, delegation, tgt
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Unconstrained delegation captures the first TGT

## Claim

A host with unconstrained delegation caches a TGT for every user who authenticates to it, including domain admins.

## Test

List hosts with the trusted for delegation flag. Coerce or wait for an admin. Read the cached tickets.

## Proof

An admin TGT is extracted and reused.

## Failure modes

Protected Users and the sensitive flag limit exposure. A printer bug needs the spooler.
