---
id: iam-passrole-is-the-role-chain
title: iam:PassRole is the role chain
tags: aws, iam, passrole
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-iam-wildcard.md
status: active
---
# iam:PassRole is the role chain

## Claim

PassRole lets a user attach a role to a service they control, and the service then runs with that role.

## Test

Read the policy for PassRole. Check which services accept a role. Create the service with the target role.

## Proof

The service executes with the target role credentials.

## Failure modes

A condition on the role or the service blocks it. A service that cannot start limits it.
