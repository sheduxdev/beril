---
id: api-openapi
title: An exposed schema is a map, not a finding
tags: api, openapi, schema
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# An exposed schema is a map, not a finding

## Claim

Swagger or OpenAPI exposes paths, parameters and models that the UI never calls. The finding is a reachable operation with weak auth.

## Test

Fetch /openapi.json and the docs UI. Diff the schema against the UI. Call undocumented methods with two roles.

## Proof

An undocumented operation returns data or performs an action.

## Failure modes

A public read-only schema is intended. A 401 on every path is not a finding.
