---
id: a-service-principal-is-a-non-human-identity
title: A service principal is a non human identity
tags: idp, service-principal, secret
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-oidc-ci.md
status: active
---
# A service principal is a non human identity

## Claim

An app registration and its service principal hold secrets, certificates and role assignments. The secret is a password.

## Test

List the app registrations and the credentials. Check the expiry and the owners. Try a client credential login.

## Proof

A token for the service principal.

## Failure modes

A certificate and a workload identity remove the secret. A short expiry limits it.
