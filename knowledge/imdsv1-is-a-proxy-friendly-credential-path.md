---
id: imdsv1-is-a-proxy-friendly-credential-path
title: IMDSv1 is a proxy friendly credential path
tags: cloud, metadata, imds
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-metadata-role.md
status: active
---
# IMDSv1 is a proxy friendly credential path

## Claim

A workload that still allows IMDSv1 can be read by any SSRF or local proxy, with no token request step.

## Test

From the workload or a proxy, GET the metadata role name and the credentials path. Compare with IMDSv2 token flow.

## Proof

Temporary credentials are returned without a token.

## Failure modes

A hop limit of one and IMDSv2 required block it. A container network can isolate metadata.
