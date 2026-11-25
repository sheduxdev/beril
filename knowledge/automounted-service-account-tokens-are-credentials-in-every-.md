---
id: automounted-service-account-tokens-are-credentials-in-every-
title: Automounted service account tokens are credentials in every pod
tags: cloud, k8s, token
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# Automounted service account tokens are credentials in every pod

## Claim

A pod with automount enabled carries a token for its service account, readable by any process and any RCE in the container.

## Test

Read `/var/run/secrets/kubernetes.io/serviceaccount/token`. Call the API with it and check the allowed verbs.

## Proof

The token authenticates to the API with the pod role.

## Failure modes

Projected short lived tokens have an audience and expiry. A read only role limits the use.
