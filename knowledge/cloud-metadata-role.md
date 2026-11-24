---
id: cloud-metadata-role
title: Cloud metadata is a credential endpoint
tags: cloud, ssrf, iam
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, labs/cloud
status: active
---
# Cloud metadata is a credential endpoint

## Claim

A workload can reach the metadata service. The returned role may have more permission than the app needs.

## Test

Query the metadata endpoint. Get the role and temporary credentials. Call get-caller-identity. Test read-only permissions.

## Proof

A read-only API response that proves the role's effective access.

## Failure modes

A role name is not a permission. IMDSv2 blocks naive requests.
