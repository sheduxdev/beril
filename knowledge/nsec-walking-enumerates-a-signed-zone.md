---
id: nsec-walking-enumerates-a-signed-zone
title: NSEC walking enumerates a signed zone
tags: dns, nsec, enumeration
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-dns.md
status: active
---
# NSEC walking enumerates a signed zone

## Claim

NSEC returns the next name in order, so repeated queries walk the zone. NSEC3 hashes the names and slows it.

## Test

Query a nonexistent name. Read the NSEC or NSEC3 record. Follow the next name ten times.

## Proof

A chain of real names from the records.

## Failure modes

NSEC3 with a high iteration count slows it. A zone with few names gives little.
