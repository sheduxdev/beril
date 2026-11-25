---
id: a-long-lived-publish-token-is-a-package-takeover
title: A long lived publish token is a package takeover
tags: supply, publish, token
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cicd-pr-target.md
status: active
---
# A long lived publish token is a package takeover

## Claim

A repository secret with an npm or PyPI publish token lets any workflow with the secret publish a new version.

## Test

Find the publish step and the secret. Check the token scope and expiry. Run a dry run publish from a branch.

## Proof

A version publishes from an untrusted branch.

## Failure modes

Trusted publishing with OIDC and a protected environment closes it. A granular token limits the packages.
