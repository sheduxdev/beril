---
id: terraform-plan-is-the-effective-cloud-change
title: Terraform plan is the effective cloud change
tags: lang, terraform, cloud
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-terraform-state.md
status: active
---
# Terraform plan is the effective cloud change

## Claim

The plan shows the real graph, the replacement and the inherited values. A module default can hide a public bucket.

## Test

Read the plan for create, replace and update. Check the public, the encryption and the policy fields. Compare with the module source.

## Proof

A planned public or unencrypted resource.

## Failure modes

A provider default can add it at apply. A policy as code can block it.
