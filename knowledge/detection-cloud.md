---
id: detection-cloud
title: Cloud detection is control-plane and role-assumption first
tags: detection, cloud, audit
confidence: high
updated: 2026-11-25
uses: 0
sources: labs/detection
status: active
---
# Cloud detection is control-plane and role-assumption first

## Claim

CreateUser, AssumeRole, policy changes and key creation are high-signal control-plane events.

## Test

Map the audit log. Baseline normal roles. Alert on new principals and permission changes.

## Proof

A sequence from a new principal to a resource action.

## Failure modes

A provider default event is noisy. A data-plane read may not appear in the control log.
