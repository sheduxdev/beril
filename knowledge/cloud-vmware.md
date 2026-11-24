---
id: cloud-vmware
title: VMware appliances are a chain of SSO and service bugs
tags: cloud, vmware, vcenter
confidence: high
updated: 2026-11-25
uses: 0
sources: references/vulnerability-research.md
status: active
---
# VMware appliances are a chain of SSO and service bugs

## Claim

vCenter SSO, the reverse proxy and the appliance services have separate parsers and trust boundaries.

## Test

Map the versions and services. Test SSO redirects, the vSphere client and the appliance API. Check known CVEs.

## Proof

An authenticated or pre-auth action beyond the intended role.

## Failure modes

A console UI bug may not affect the API. Version mapping matters.
