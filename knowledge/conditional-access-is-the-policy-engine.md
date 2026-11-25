---
id: conditional-access-is-the-policy-engine
title: Conditional access is the policy engine
tags: idp, conditional-access, policy
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Conditional access is the policy engine

## Claim

The policy decides by user, device, location and app. A policy in report only mode or an excluded group is a gap.

## Test

Read the policies and the states. Check the exclusions. Try a login from a location and a device outside the rule.

## Proof

A login the policy should block.

## Failure modes

A report only policy logs and allows. A compliant device can pass.
