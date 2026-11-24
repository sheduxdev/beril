---
id: eng-api-contract
title: An API is a promise about errors and time
tags: engineering, api, contract
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An API is a promise about errors and time

## Claim

Inputs, outputs, status codes, idempotency and latency are part of the contract. A version change is a migration.

## Test

Write the contract before the handler. Test the error and timeout cases. Diff the schema.

## Proof

A consumer can code against the contract without reading the implementation.

## Failure modes

A 200 with an error body breaks the promise.
