---
id: web-cors-null-origin
title: CORS reflection is only a bug with credentials
tags: web, cors, browser
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# CORS reflection is only a bug with credentials

## Claim

The server reflects any Origin, or trusts null, while allowing credentials. Any site can read authenticated responses.

## Test

Send Origin: https://evil.lab and Origin: null. Check ACAO and ACAC. Read a private endpoint from a cross-origin page.

## Proof

A browser fetch returns private data for a logged-in victim.

## Failure modes

Wildcard ACAO with ACAC true is invalid. A public endpoint with no credentials is not a finding.
