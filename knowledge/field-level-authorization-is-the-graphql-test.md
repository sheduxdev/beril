---
id: field-level-authorization-is-the-graphql-test
title: Field level authorization is the GraphQL test
tags: web, graphql, authorization
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-graphql-field-auth.md, knowledge/api-partial-update.md
status: active
---
# Field level authorization is the GraphQL test

## Claim

Object level checks do not cover a field. A user can read a cost, token or internal note on an object they own.

## Test

Request every field on one object with a low privilege token. Compare with the admin view.

## Proof

A field returns data the role should not see.

## Failure modes

A field resolver can mask by role. A null can be intended.
