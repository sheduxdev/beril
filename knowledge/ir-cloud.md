---
id: ir-cloud
title: Cloud audit logs are the timeline
tags: ir, cloud, logs
confidence: medium
updated: 2026-11-24
uses: 0
sources: labs/detection
status: active
---
# Cloud audit logs are the timeline

## Claim

CloudTrail, Activity Log or audit logs record the control plane. Data plane and identity events need separate sources.

## Test

Collect control plane, identity and network logs. Normalize to UTC. Correlate role assumption with resource access.

## Proof

A sequence from credential to action with source ids.

## Failure modes

A disabled or short-retention log leaves a gap. A resource event can have no control-plane event.
