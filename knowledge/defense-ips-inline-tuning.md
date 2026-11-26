---
id: defense-ips-inline-tuning
title: An inline IPS needs an alert-only baseline first
tags: defense, ips, suricata, snort
confidence: high
updated: 2026-11-26
uses: 0
sources: https://docs.suricata.io/, https://www.snort.org/documents, https://csrc.nist.gov/pubs/sp/800/94/final
status: active
---
# An inline IPS needs an alert-only baseline first

## Claim

Suricata or Snort in IPS mode drops traffic on a rule match, so an untuned ruleset breaks production before it stops an attacker.

## Test

Run the ruleset in IDS mode. Rank rules by alert count. Suppress or threshold noisy rules with a note. Switch to drop per rule category.

## Proof

A replayed exploit pcap is dropped and a normal-day pcap passes.

## Failure modes

TLS hides payload rules unless traffic is decrypted. An IPS that fails closed under load is an outage.
