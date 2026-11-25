---
id: gcp-workload-identity-binds-a-kubernetes-subject
title: GCP workload identity binds a Kubernetes subject
tags: gcp, workload-identity, k8s
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-oidc-ci.md
status: active
---
# GCP workload identity binds a Kubernetes subject

## Claim

The principal is a service account and the condition is the Kubernetes service account and namespace. A wildcard trusts the whole cluster.

## Test

Read the binding condition. Compare with the annotated service account. Try another namespace.

## Proof

A token from the wrong namespace assumes the account.

## Failure modes

A strict subject and namespace condition closes it. A cluster wide scope is required.
