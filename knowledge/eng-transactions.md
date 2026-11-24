---
id: eng-transactions
title: A transaction is a boundary, not a decoration
tags: engineering, database, transactions
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A transaction is a boundary, not a decoration

## Claim

The unit of consistency is the transaction. A side effect outside it can commit while the transaction rolls back.

## Test

List the writes and the external calls. Move the external call out or add compensation.

## Proof

A failure leaves the system in one consistent state.

## Failure modes

A distributed transaction without a protocol is a hope.
