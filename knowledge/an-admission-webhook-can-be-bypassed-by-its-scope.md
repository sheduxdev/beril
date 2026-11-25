---
id: an-admission-webhook-can-be-bypassed-by-its-scope
title: An admission webhook can be bypassed by its scope
tags: k8s, admission, policy
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# An admission webhook can be bypassed by its scope

## Claim

A webhook with a narrow namespace selector, a missing failure policy or an ignored operation lets the excluded objects through.

## Test

Read the webhook config. Check the selector, the operations and the failure policy. Create an excluded pod.

## Proof

A policy violating pod is admitted.

## Failure modes

A fail closed policy with a full selector holds. A second controller can catch it.
