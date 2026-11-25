---
id: scim-is-a-provisioning-api-with-a-token
title: SCIM is a provisioning API with a token
tags: idp, scim, token
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# SCIM is a provisioning API with a token

## Claim

The SCIM token creates, updates and deletes users and groups. A leaked token is a tenant user admin.

## Test

Read the SCIM endpoint and the token owner. List the users. Create a test user and delete it.

## Proof

A user created through SCIM.

## Failure modes

A scope limited token can only read. An IP allowlist narrows the use.
