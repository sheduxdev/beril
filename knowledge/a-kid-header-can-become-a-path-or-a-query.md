---
id: a-kid-header-can-become-a-path-or-a-query
title: A kid header can become a path or a query
tags: auth, jwt, kid
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/web-jwt-signature-trust.md
status: active
---
# A kid header can become a path or a query

## Claim

If kid selects a key file or a database row, traversal or injection in kid can choose the key or break the lookup.

## Test

Send kid values with ../, a known file path, a quote and a null byte. Watch the error and the signature result.

## Proof

A token verifies with a key you supplied or a path you reached.

## Failure modes

A fixed key map ignores kid. Some libraries sanitize the path.
