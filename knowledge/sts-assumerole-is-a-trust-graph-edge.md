---
id: sts-assumerole-is-a-trust-graph-edge
title: sts:AssumeRole is a trust graph edge
tags: aws, sts, trust
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-iam-wildcard.md
status: active
---
# sts:AssumeRole is a trust graph edge

## Claim

A role that trusts the current identity can be assumed directly, and the trust policy is the whole check.

## Test

Read the assume role policy of each role. Find a principal you control. Call AssumeRole and check the session.

## Proof

A session with the target role.

## Failure modes

An external id or a source account condition blocks it. A permission boundary limits the session.
