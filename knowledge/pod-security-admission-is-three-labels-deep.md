---
id: pod-security-admission-is-three-labels-deep
title: Pod Security Admission is three labels deep
tags: k8s, psa, namespace
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# Pod Security Admission is three labels deep

## Claim

A namespace with the privileged level or a missing label runs host path, host network and privileged pods.

## Test

Read the namespace labels. Create a pod with a hostPath and privileged true. Check the admission result.

## Proof

The privileged pod is admitted.

## Failure modes

A restricted level and a version label hold. A webhook can override.
