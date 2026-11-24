---
id: web-graphql-field-auth
title: GraphQL authorization is per field, not per endpoint
tags: web, graphql, api
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/bug-method-matrix.md
status: active
---
# GraphQL authorization is per field, not per endpoint

## Claim

The gateway checks the query but resolvers do not check the object, field or mutation. Introspection is a map, not a finding.

## Test

Test each field and mutation with two roles. Test node lookups, nested fields, aliases, batching and cost limits.

## Proof

A restricted field or mutation returns data for a lower-privilege account.

## Failure modes

Introspection enabled is not a bug. HTTP 200 with GraphQL errors is not success.
