---
id: a-wildcard-redirect-uri-is-a-claimable-subdomain
title: A wildcard redirect URI is a claimable subdomain
tags: auth, oauth, redirect
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md, knowledge/a-dangling-cname-is-a-takeover-lead-not-a-finding.md
status: active
---
# A wildcard redirect URI is a claimable subdomain

## Claim

A redirect pattern like https://*.example.com lets any subdomain, including a dangling one, receive the code.

## Test

List the redirect rules. Find a subdomain that is dangling or user controlled. Send the flow through it.

## Proof

The code arrives at the host you control.

## Failure modes

A wildcard that only matches existing hosts is narrower. Path checks can still be bypassed with traversal.
