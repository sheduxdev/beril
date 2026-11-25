---
id: overlayfs-is-a-merge-of-layers
title: Overlayfs is a merge of layers
tags: link, overlayfs, container
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-k8s-hostpath.md
status: active
---
# Overlayfs is a merge of layers

## Claim

The upper and lower layers merge into one view. A copy up or a whiteout in a shared layer can change the container filesystem.

## Test

Read the mount options and the layers. Create a file and watch the copy up. Check the upper dir.

## Proof

A copied file in the upper layer.

## Failure modes

A read only lower blocks the copy. A user namespace can change the owner.
