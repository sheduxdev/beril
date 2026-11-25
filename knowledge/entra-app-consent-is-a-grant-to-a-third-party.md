---
id: entra-app-consent-is-a-grant-to-a-third-party
title: Entra app consent is a grant to a third party
tags: idp, entra, consent
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-azure-role.md
status: active
---
# Entra app consent is a grant to a third party

## Claim

A user consent grants an app the scopes it asks for, including mail or file read, without an admin.

## Test

Read the app scopes and the consent policy. Consent with a test user. Read a resource with the granted token.

## Proof

A token with the user scopes and a resource read.

## Failure modes

An admin consent policy blocks the user. A low scope app is harmless.
