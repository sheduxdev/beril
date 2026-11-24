---
id: process-scope-parse
title: Scope is a list of rules, not a domain
tags: process, scope, recon
confidence: high
updated: 2026-11-24
uses: 0
sources: docs/break-my-app.md
status: active
---
# Scope is a list of rules, not a domain

## Claim

Wildcards, exclusions, acquisitions and third-party hosts change what is in scope. A subdomain is not automatically owned.

## Test

Parse the program brief into allow and deny rules. Resolve every asset. Check the ownership evidence.

## Proof

An asset with a scope citation before the first request.

## Failure modes

A shared CDN or cloud IP belongs to many customers. A parent domain does not imply a sibling.
