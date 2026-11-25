---
id: a-helm-chart-can-run-a-hook
title: A Helm chart can run a hook
tags: pkg, helm, hook
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# A Helm chart can run a hook

## Claim

A pre or post install hook is a pod with the chart values. A hook can run an image and a command before the app.

## Test

Read the hook manifests and the values. Render the chart. Check the hook image and the service account.

## Proof

A hook pod action in the namespace.

## Failure modes

A hook with no hook weight can be ignored. A policy can block the image.
