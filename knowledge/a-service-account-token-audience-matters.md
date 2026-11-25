---
id: a-service-account-token-audience-matters
title: A service account token audience matters
tags: k8s, serviceaccount, token
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# A service account token audience matters

## Claim

A projected token with an audience is only accepted by that audience. A legacy token without one is broader.

## Test

Decode the token claims. Read the audience and the expiry. Call the API and a non API audience.

## Proof

A token accepted outside the intended audience.

## Failure modes

A short expiry and a strict audience limit it. A legacy secret token is long lived.
