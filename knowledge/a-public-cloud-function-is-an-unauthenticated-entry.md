---
id: a-public-cloud-function-is-an-unauthenticated-entry
title: A public Cloud Function is an unauthenticated entry
tags: gcp, function, auth
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-serverless.md
status: active
---
# A public Cloud Function is an unauthenticated entry

## Claim

A function with `allUsers` invoker allows anonymous calls and the function code runs with its service account.

## Test

Read the IAM policy. Call the URL without a token. Read the function environment and role.

## Proof

A successful unauth call and the runtime identity.

## Failure modes

An API gateway or a load balancer can add auth. A function with a narrow role limits impact.
