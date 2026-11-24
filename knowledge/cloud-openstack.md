---
id: cloud-openstack
title: OpenStack policy is a service and project graph
tags: cloud, openstack, keystone
confidence: low
updated: 2026-11-25
uses: 0
sources: references/vulnerability-research.md
status: active
---
# OpenStack policy is a service and project graph

## Claim

Keystone issues a scoped token; policy.json decides the action. A role at the wrong scope crosses projects.

## Test

Read the token scope. Check the policy. Test a read in another project.

## Proof

A token that works outside its project.

## Failure modes

A default policy is often permissive. Admin tokens hide scope bugs.
