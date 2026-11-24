---
id: web-xxe-parser
title: XXE depends on entity expansion and the parser feature set
tags: web, xxe, xml
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# XXE depends on entity expansion and the parser feature set

## Claim

A parser resolves external entities, or resolves them only for a nested format such as SVG, DOCX or SAML.

## Test

Send a DOCTYPE with a file entity. Try parameter entities and OOB when the response hides the value.

## Proof

A local file or a callback from the parser.

## Failure modes

An XML parser with entities disabled is not vulnerable. JSON endpoints are out of scope.
