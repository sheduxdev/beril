---
id: a-dangling-cname-is-a-takeover-lead-not-a-finding
title: A dangling CNAME is a takeover lead, not a finding
tags: recon, dns, takeover
confidence: high
updated: 2026-11-25
uses: 0
sources: references/artex-flask.md
status: active
---
# A dangling CNAME is a takeover lead, not a finding

## Claim

A CNAME to a service plus that service's unclaimed-page marker means the hostname can be claimed by someone else. The CNAME alone only proves the pointer.

## Test

Resolve CNAME, fetch the host, compare the body with the service marker, then try to claim the resource at the provider. A 404 with the marker is the strong case.

## Proof

CNAME to the service and its exact unclaimed page on the hostname, confirmed by a claim attempt.

## Failure modes

A live but parked service looks the same. A custom domain already attached at the provider stays claimed. Wildcard DNS hides the CNAME.
