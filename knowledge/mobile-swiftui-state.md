---
id: mobile-swiftui-state
title: SwiftUI state is not a security boundary
tags: mobile, ios, swiftui
confidence: low
updated: 2026-11-24
uses: 0
sources: references/mobile-reverse.md
status: active
---
# SwiftUI state is not a security boundary

## Claim

The UI hides a control but the state or API still accepts the action. Deep links can set a route.

## Test

Map scenes and routes. Trigger the deep link. Call the API directly with the state the UI hides.

## Proof

An action or screen the UI should not allow.

## Failure modes

A hidden button is not a server-side control. Test the API.
