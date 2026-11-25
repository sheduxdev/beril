---
id: a-nested-object-id-often-checks-the-parent-only
title: A nested object id often checks the parent only
tags: api, bola, authorization
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/api-partial-update.md, references/techniques.md
status: active
---
# A nested object id often checks the parent only

## Claim

Routes like /orgs/1/projects/2 check org membership and forget the project owner, so a project from another org is readable.

## Test

Keep your org id, swap the child id to a foreign object. Repeat for write and delete.

## Proof

The foreign child object is returned or changed.

## Failure modes

A global child lookup can be intended. Confirm the object belongs to another tenant.
