---
id: irsa-trust-must-pin-the-service-account-subject
title: IRSA trust must pin the service account subject
tags: cloud, k8s, irsa
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-eks.md, knowledge/cloud-oidc-ci.md
status: active
---
# IRSA trust must pin the service account subject

## Claim

An OIDC trust policy that matches on the issuer alone lets any service account in the cluster assume the role.

## Test

Read the trust policy condition. Compare the `sub` value with the annotated service account and namespace.

## Proof

A pod in another namespace assumes the role.

## Failure modes

A wildcard on the service account name is common and can be intended. Audience checks can narrow it.
