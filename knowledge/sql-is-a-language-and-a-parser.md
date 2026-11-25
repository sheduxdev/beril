---
id: sql-is-a-language-and-a-parser
title: SQL is a language and a parser
tags: lang, sql, injection
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-sqli-parameterized.md
status: active
---
# SQL is a language and a parser

## Claim

A parameterized query fixes values, not identifiers. An ORDER BY, a table name or a column name needs an allowlist.

## Test

Find the dynamic identifier. Send a sort parameter, a table and a column. Add a quote and a comment.

## Proof

A changed order or a syntax error from the identifier.

## Failure modes

A hardcoded map closes it. A driver can quote an identifier for you.
