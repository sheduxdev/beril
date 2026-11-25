---
id: mass-assignment-needs-the-role-field-in-the-schema
title: Mass assignment needs the role field in the schema
tags: api, mass-assignment, authorization
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/api-mass-assignment.md
status: active
---
# Mass assignment needs the role field in the schema

## Claim

A framework that binds the request body to the model lets an unlisted field such as role, tenant or verified through.

## Test

Add one field at a time to an update call. Start with role, owner, tenant, balance, email_verified.

## Proof

The added field changes and survives a read.

## Failure modes

A strict DTO blocks it. Some fields change but are ignored by authorization.
