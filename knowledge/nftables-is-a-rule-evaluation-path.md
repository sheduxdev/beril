---
id: nftables-is-a-rule-evaluation-path
title: nftables is a rule evaluation path
tags: link, nftables, network
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# nftables is a rule evaluation path

## Claim

The ruleset evaluates expressions and sets in order. A set with a timeout or a map update is a race and a state surface.

## Test

List the tables and the chains. Read the expressions. Update a set entry and watch the rule path.

## Proof

A packet allowed or dropped by the changed set.

## Failure modes

A default drop holds. A hardware offload can change the path.
