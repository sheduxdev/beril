---
id: unencrypted-etcd-secrets-are-readable-from-a-snapshot
title: Unencrypted etcd secrets are readable from a snapshot
tags: cloud, k8s, etcd
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-secrets.md
status: active
---
# Unencrypted etcd secrets are readable from a snapshot

## Claim

Without encryption at rest, every Secret is plaintext in an etcd backup, including service account tokens and keys.

## Test

Check the encryption config on the API server. Take a snapshot in a lab and read the secret keys.

## Proof

A secret value appears in the snapshot.

## Failure modes

KMS encryption or an external secret store closes it. A snapshot from a managed control plane can be opaque.
