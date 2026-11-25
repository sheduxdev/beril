---
id: db2-on-z-os-uses-the-racf-identity
title: DB2 on z/OS uses the RACF identity
tags: mf, db2, access
confidence: low
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# DB2 on z/OS uses the RACF identity

## Claim

The DB2 grant and the RACF profile both decide. A table grant without the RACF right still fails.

## Test

Read the table grants and the RACF profiles. Try a select with the current id. Compare with the grant.

## Proof

A read allowed by both layers.

## Failure modes

A view can hide the table. A plan can run with the owner rights.
