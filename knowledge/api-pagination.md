---
id: api-pagination
title: Pagination is an enumeration and counting oracle
tags: api, pagination, enumeration
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# Pagination is an enumeration and counting oracle

## Claim

Offset pagination leaks total counts and allows skipping; cursor pagination leaks stable ids and can be replayed.

## Test

Compare total fields across queries. Walk pages with a changed filter. Try a negative or huge offset.

## Proof

A full dataset or a count the user should not see.

## Failure modes

A capped total is not a leak. A cursor that is opaque but stable is still enumerable.
