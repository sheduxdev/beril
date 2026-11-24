---
id: cicd-pr-target
title: pull_request_target can run untrusted code with a write token
tags: supply-chain, ci, github-actions
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/cloud
status: active
---
# pull_request_target can run untrusted code with a write token

## Claim

The workflow uses pull_request_target, checks out the PR head and runs code with repository secrets or write permissions.

## Test

Read the workflow. Open a PR from a fork. Change a script it runs. Watch the token and secrets.

## Proof

A secret exfiltration or a push from the PR code.

## Failure modes

pull_request_target with no checkout of the head is safe. A read-only token limits impact.
