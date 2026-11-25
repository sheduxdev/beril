---
id: azure-managed-identity-is-a-token-endpoint
title: Azure managed identity is a token endpoint
tags: azure, managed-identity, token
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-metadata-role.md
status: active
---
# Azure managed identity is a token endpoint

## Claim

The IMDS endpoint returns an access token for the attached identity to any process on the VM.

## Test

Request the metadata endpoint with the resource parameter. Read the token and call the resource.

## Proof

A token accepted by the target resource.

## Failure modes

A required IMDS header or an identity scope limits it. A user assigned identity needs the client id.
