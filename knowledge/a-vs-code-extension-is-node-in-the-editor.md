---
id: a-vs-code-extension-is-node-in-the-editor
title: A VS Code extension is Node in the editor
tags: pkg, vscode, extension
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A VS Code extension is Node in the editor

## Claim

An extension runs with the editor user and can read the workspace, the settings and the network. A marketplace install is a trust decision.

## Test

Read the manifest and the activation events. Check the publisher and the install count. Run the extension in a clean profile.

## Proof

A file or a network action from the extension.

## Failure modes

A workspace trust prompt limits it. A verified publisher raises trust.
