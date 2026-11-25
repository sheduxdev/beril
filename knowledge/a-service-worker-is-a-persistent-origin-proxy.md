---
id: a-service-worker-is-a-persistent-origin-proxy
title: A service worker is a persistent origin proxy
tags: browser, service-worker, cache
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A service worker is a persistent origin proxy

## Claim

A registered worker sees fetches after activation and can serve a stale or crafted response across tabs.

## Test

List registrations. Read the fetch handler. Go offline and load a page. Check the cache names and the update path.

## Proof

A response is served by the worker, not the network.

## Failure modes

A short max age and a skipWaiting flow limit staleness. A scope limit narrows the origin area.
