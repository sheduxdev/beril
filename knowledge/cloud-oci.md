---
id: cloud-oci
title: OCI policy is compartment and tenancy scoped
tags: cloud, oci, iam
confidence: low
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# OCI policy is compartment and tenancy scoped

## Claim

Instance principals and dynamic groups grant rights through policy statements at a compartment or tenancy scope.

## Test

Read the dynamic group and policy. Check the compartment path. Test a read at the highest scope.

## Proof

A read or token mint outside the intended compartment.

## Failure modes

A policy on a single compartment is narrow. A tenancy-wide manage statement is not.
