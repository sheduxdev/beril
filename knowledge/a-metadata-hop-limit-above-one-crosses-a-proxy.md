---
id: a-metadata-hop-limit-above-one-crosses-a-proxy
title: A metadata hop limit above one crosses a proxy
tags: cloud, metadata, ssrf
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-metadata-role.md
status: active
---
# A metadata hop limit above one crosses a proxy

## Claim

The default hop limit of one blocks a forwarded request. A raised limit lets a proxy or a nested container reach IMDS.

## Test

Read the instance metadata options. Request credentials from a proxy or a second network namespace.

## Proof

Credentials arrive through the extra hop.

## Failure modes

A sidecar that strips the token header blocks IMDSv2. An egress rule can deny the address.
