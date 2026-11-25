---
id: terraform-providers-are-downloaded-code
title: Terraform providers are downloaded code
tags: pkg, terraform, provider
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-terraform-state.md
status: active
---
# Terraform providers are downloaded code

## Claim

A provider is a binary that runs with the plan rights. A version range or a mirror can supply a different build.

## Test

Read the provider lock file and the source. Check the checksum. Run a plan with a network monitor.

## Proof

A provider call from the plan.

## Failure modes

A lock file and a signed mirror hold. A local provider can be intentional.
