---
id: mobile-provider-paths
title: An exported provider with a broad path leaks files
tags: mobile, android, provider
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/mobile
status: active
---
# An exported provider with a broad path leaks files

## Claim

A FileProvider is exported and its paths include a wide directory such as external storage root.

## Test

Read the provider XML. Request a path outside the intended directory with a content resolver.

## Proof

A file read through the provider that the app did not intend to share.

## Failure modes

A provider with grantUriPermissions and narrow paths is safer. A non-exported provider needs a grant.
