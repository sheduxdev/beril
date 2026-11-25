---
id: an-exported-component-without-a-permission-is-open-to-every-
title: An exported component without a permission is open to every app
tags: mobile, android, exported
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mobile-deep-link-bridge.md, labs/mobile
status: active
---
# An exported component without a permission is open to every app

## Claim

`android:exported=true` with no signature permission lets any installed app start the component and pass the intent extras.

## Test

Read the manifest. Start the component with adb and with a small helper app. Pass each extra the code reads.

## Proof

The action runs or data returns without the target app in front.

## Failure modes

A permission on the component closes it. A deep link filter can still expose a narrow path.
