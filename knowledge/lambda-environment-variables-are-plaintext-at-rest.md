---
id: lambda-environment-variables-are-plaintext-at-rest
title: Lambda environment variables are plaintext at rest
tags: aws, lambda, secret
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-serverless.md
status: active
---
# Lambda environment variables are plaintext at rest

## Claim

Environment variables are visible to anyone with read on the function config and in the console, even when the code is private.

## Test

Read the function config. Check the variables and the KMS key. Compare with the role permissions.

## Proof

A live token in the environment.

## Failure modes

A KMS encrypted variable hides it from a plain read. A short lived token limits the value.
