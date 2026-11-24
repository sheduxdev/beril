---
id: cloud-terraform-state
title: Terraform state is a secret store
tags: cloud, terraform, state
confidence: medium
updated: 2026-11-24
uses: 0
sources: labs/cloud
status: active
---
# Terraform state is a secret store

## Claim

The state file holds resource attributes, connection strings and sometimes plaintext secrets. A public bucket or repo leaks it.

## Test

Find the backend. Check access. Grep state for passwords, keys and endpoints.

## Proof

A secret from state used against the resource.

## Failure modes

An encrypted remote backend with narrow access is safer. Lock files matter for integrity.
