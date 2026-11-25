---
id: scope-is-a-technical-control-not-paperwork
title: Scope is a technical control, not paperwork
tags: senior, scope, authorization
confidence: high
updated: 2026-11-26
uses: 0
sources: docs/verification.md, references/senior-bar.md
status: active
---
# Scope is a technical control, not paperwork

## Claim

The ownership record and scope file decide which host, path and method is legal. They belong in the test plan, not in a folder.

## Test

Resolve the exact host, check the record, load the scope, and stop when a redirect leaves it. Record the check in the report.

## Proof

A scope line and an authorization record that match the request.

## Failure modes

A redirect to a sibling host. A CDN shared IP. A wildcard scope that hides a third party.
