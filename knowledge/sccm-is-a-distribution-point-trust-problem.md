---
id: sccm-is-a-distribution-point-trust-problem
title: SCCM is a distribution point trust problem
tags: win, sccm, deployment
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# SCCM is a distribution point trust problem

## Claim

An SCCM client that trusts a distribution point or a policy without signing accepts a package from an attacker.

## Test

Read the client policy and the DP list. Check the package signing and the network access account.

## Proof

A package runs on the client from the attacker DP.

## Failure modes

HTTPS only and package signing close it. A hardened site server is a different target.
