---
id: a-gcp-service-account-key-is-a-long-lived-identity
title: A GCP service account key is a long lived identity
tags: gcp, service-account, key
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-gcp-iam.md
status: active
---
# A GCP service account key is a long lived identity

## Claim

A downloaded service account key is a JSON credential with no expiry and the full rights of the account.

## Test

Find key files in repos and buckets. Use gcloud with the key. Enumerate the roles.

## Proof

An authenticated session as the service account.

## Failure modes

Key rotation and org policy can stop new keys. Workload identity removes the file.
