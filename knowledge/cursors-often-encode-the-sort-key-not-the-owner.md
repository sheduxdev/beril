---
id: cursors-often-encode-the-sort-key-not-the-owner
title: Cursors often encode the sort key, not the owner
tags: api, cursor, authorization
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/api-cursor.md, knowledge/api-pagination.md
status: active
---
# Cursors often encode the sort key, not the owner

## Claim

A cursor that is only base64 of a timestamp and id can be forged to read another tenant's page.

## Test

Decode the cursor. Change the id or time. Send it with your token.

## Proof

The page returns foreign records.

## Failure modes

A signed cursor or a server side filter closes it. Leaky ordering can still reveal counts.
