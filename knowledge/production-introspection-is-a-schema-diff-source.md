---
id: production-introspection-is-a-schema-diff-source
title: Production introspection is a schema diff source
tags: api, graphql, recon
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Production introspection is a schema diff source

## Claim

Introspection exposes deprecated and internal fields that the UI never calls. They are the best place to test field authorization.

## Test

Dump the schema. Diff it against the public docs. Call deprecated and mutation fields with a low privilege token.

## Proof

A field returns data the UI does not show.

## Failure modes

Introspection can be disabled and still leak in errors. A field can be public by design.
