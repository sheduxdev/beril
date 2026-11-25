---
id: a-public-gcs-object-ignores-the-bucket-iam
title: A public GCS object ignores the bucket IAM
tags: gcp, storage, acl
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-gcp-iam.md
status: active
---
# A public GCS object ignores the bucket IAM

## Claim

`allUsers` on the object ACL gives anonymous read even when the bucket is uniform access and private.

## Test

Read the object ACL. Fetch without a token. Check the bucket uniform access setting.

## Proof

An anonymous read of the object.

## Failure modes

Uniform bucket level access disables object ACLs. A signed URL can look public but expire.
