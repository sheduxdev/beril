---
id: cloud-serverless
title: Serverless events are input, not a trusted trigger
tags: cloud, serverless, lambda
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Serverless events are input, not a trusted trigger

## Claim

A function trusts the event shape, the source ARN or the authorizer, and passes fields into a shell or SDK call.

## Test

Invoke with a modified event. Test the authorizer. Check the execution role.

## Proof

A function action or read beyond the intended event.

## Failure modes

A function URL with IAM auth is different from an open one. Check the trigger.
