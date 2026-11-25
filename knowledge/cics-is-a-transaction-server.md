---
id: cics-is-a-transaction-server
title: CICS is a transaction server
tags: mf, cics, transaction
confidence: low
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# CICS is a transaction server

## Claim

A CICS transaction id maps to a program. A weak transaction or a debug transaction reaches the data.

## Test

List the transactions and the programs. Try a read transaction. Check the debug and the file control.

## Proof

A record from a transaction.

## Failure modes

A transaction can be disabled. A region can be isolated.
