---
id: least-privilege-is-a-per-request-budget
title: Least privilege is a per request budget
tags: design, least-privilege, iam
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-iam-wildcard.md
status: active
---
# Least privilege is a per request budget

## Claim

A service that holds administrator rights for one rare action gives every request the same reach. The right must be per call or per workload.

## Test

Read the runtime role. List the actions the request path uses. Compare with the granted set. Find one unused admin right.

## Proof

A role with the action list reduced to the path.

## Failure modes

A shared role can serve several paths. A break glass role is intentional.
