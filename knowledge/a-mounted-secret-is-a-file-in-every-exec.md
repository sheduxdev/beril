---
id: a-mounted-secret-is-a-file-in-every-exec
title: A mounted secret is a file in every exec
tags: k8s, secret, mount
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-secrets.md
status: active
---
# A mounted secret is a file in every exec

## Claim

A secret volume is readable by any process in the container, including a shell from an RCE.

## Test

List the mounts. Read the secret file. Compare with the env vars. Check the file mode.

## Proof

A plaintext secret from the mount.

## Failure modes

A projected short lived token limits it. An external secret store can keep the value out.
