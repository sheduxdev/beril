---
id: a-certificate-name-is-not-a-live-host
title: A certificate name is not a live host
tags: osint, certificate, dns
confidence: high
updated: 2026-11-26
uses: 0
sources: references/osint-toolkit.md, knowledge/a-dangling-cname-is-a-takeover-lead-not-a-finding.md
status: active
---
# A certificate name is not a live host

## Claim

Certificate transparency lists names that were issued, not names that resolve today. A dead name is still useful as history.

## Test

Take a CT name. Resolve it. Probe it. Mark live, dead or wildcard.

## Proof

A resolution and an HTTP status per name.

## Failure modes

A wildcard can resolve every name. A split horizon can hide the public record.
