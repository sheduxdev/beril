---
id: web-sqli-parameterized
title: SQL injection is a string-built query at a boundary
tags: web, sqli, database
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/bug-method-matrix.md
status: active
---
# SQL injection is a string-built query at a boundary

## Claim

User input reaches a query without a parameter binding. Escaping can fail when the charset, collation or parser changes.

## Test

Establish true and false baselines. Test quote, comment and parenthesis behavior. Move to time or OOB only when union and error are blocked.

## Proof

A bounded extraction of a value the tester should not see, with request and response.

## Failure modes

A WAF block looks like a false condition. Network jitter looks like a time delay. Do not dump the database.
