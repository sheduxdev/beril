---
id: a-zone-transfer-is-a-full-inventory
title: A zone transfer is a full inventory
tags: dns, axfr, inventory
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# A zone transfer is a full inventory

## Claim

An NS that allows AXFR returns every record in the zone, including internal names.

## Test

List the NS. Try `dig AXFR` against each. Compare with the public names.

## Proof

A zone file with records not in the public list.

## Failure modes

A split horizon can show a public subset. A primary only allowlist blocks it.
