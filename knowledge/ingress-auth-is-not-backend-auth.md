---
id: ingress-auth-is-not-backend-auth
title: Ingress auth is not backend auth
tags: k8s, ingress, auth
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-service-mesh.md
status: active
---
# Ingress auth is not backend auth

## Claim

An auth annotation on an Ingress protects only the paths it matches. A service reached by port forward or a second ingress is open.

## Test

Read the ingress rules. Compare with the services. Port forward the service and call it directly.

## Proof

A backend response without the ingress auth.

## Failure modes

A service mesh with mTLS and authz closes it. A cluster IP only service is internal.
