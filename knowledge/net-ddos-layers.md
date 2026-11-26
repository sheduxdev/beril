---
id: net-ddos-layers
title: DDoS defense matches the layer the attack targets
tags: net, ddos, availability
confidence: high
updated: 2026-11-26
uses: 0
sources: https://www.cisa.gov/sites/default/files/2024-03/UPDATED_Joint-DDoS_Guide_03192024_508c%20%281%29.pdf, https://www.cisa.gov/resources-tools/resources/understanding-and-responding-distributed-denial-service-attacks
status: active
---
# DDoS defense matches the layer the attack targets

## Claim

CISA, FBI and MS-ISAC split DDoS into three types: volumetric (consume bandwidth, e.g. DNS reflection), protocol (exhaust state at layers 3 and 4, e.g. SYN flood), and application (layer 7, cheap requests that cost the server dearly). A control for one does little for another.

## Test

Classify the last incident or a tabletop by type. Check upstream scrubbing or anycast for volumetric, SYN cookies and connection limits for protocol, and rate limits plus caching and bot scoring for layer 7.

## Proof

A mitigation mapped to each type, with capacity above the expected flood and a provider that can absorb volumetric traffic you cannot.

## Failure modes

An on-box firewall cannot stop a volumetric flood that fills the pipe upstream. Layer 7 attacks pass as valid requests, so signatures miss them. The three types combine in one campaign.
