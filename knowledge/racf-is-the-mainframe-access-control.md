---
id: racf-is-the-mainframe-access-control
title: RACF is the mainframe access control
tags: mf, racf, access
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# RACF is the mainframe access control

## Claim

RACF profiles grant the dataset and the transaction rights. A broad profile or a special attribute is the path.

## Test

List the user attributes and the profiles. Check the group. Try a dataset read outside the intended set.

## Proof

A dataset or a transaction outside the role.

## Failure modes

A strict profile and a protected user hold. A special attribute needs an approval.
