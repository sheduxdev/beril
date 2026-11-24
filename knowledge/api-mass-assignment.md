---
id: api-mass-assignment
title: Mass assignment is a binder trusting extra fields
tags: api, json, mass-assignment
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Mass assignment is a binder trusting extra fields

## Claim

A framework binds the request body to an object with more fields than the UI sends, such as role or balance.

## Test

Add one extra field at a time. Compare the object before and after. Try nested objects and arrays.

## Proof

A field changes that the UI never exposed.

## Failure modes

A field that is ignored is not mass assignment. Read the serializer or schema.
