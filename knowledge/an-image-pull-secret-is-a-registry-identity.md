---
id: an-image-pull-secret-is-a-registry-identity
title: An image pull secret is a registry identity
tags: k8s, registry, secret
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-secrets.md
status: active
---
# An image pull secret is a registry identity

## Claim

The pull secret holds a registry credential and is mounted or referenced in the pod spec, readable to anyone with pod read.

## Test

Read the pod spec. Read the secret. Use the credential against the registry and list the repos.

## Proof

A registry login.

## Failure modes

A short lived token limits it. A public registry makes the secret low value.
