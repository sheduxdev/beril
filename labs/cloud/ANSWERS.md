# Cloud lab answers

## 1. `terraform validate`

It checks syntax and provider schema. It does not check security posture, public access, or IAM breadth.

## 2. S3 ACL

`public-read` makes every object readable by anyone on the internet. A report bucket with customer data is a breach. Check whether the bucket has a policy that blocks public access later.

## 3. Security group

Port 22 and port 80 are open to `0.0.0.0/0`. SSH open to the world is the larger brute-force and credential-stuffing surface. Port 80 is expected for a web lab but should redirect to 443.

## 4. Public database

`publicly_accessible = true` gives the instance a public endpoint. Combined with a static password and no mention of a security group, the database is reachable from the internet if the network allows it.

## 5. IAM

`Action: "*"` with `Resource: "*"` is administrator access. A leaked deployment credential can read data, change IAM, and delete resources.

## 6. Pod

`privileged: true` gives all capabilities and device access. `runAsUser: 0` is root inside the container. Together, a container escape is much easier and root maps to host root in many configurations.

## 7. Host mount

A shell can read `/etc/shadow`, the kubelet config, service account tokens, and every host filesystem path. It can write to host cron, binaries, or the container runtime socket if present.

## 8. `node:latest`

The tag moves. A rebuild can pull a different major version and break or change the runtime. Use a version and a digest.

## 9. `ENV API_KEY`

`ENV` is visible in `docker inspect` and in the image history. Build arguments and env are not secrets. Use a runtime secret or a secret manager. If the key is a public client key, document that.

## 10. Findings

| Finding | Severity | Fix |
|---|---|---|
| Public S3 ACL | High | Block public access unless the bucket is a static public site |
| SSH open to the world | Medium | Restrict to a bastion or known ranges |
| Public database with static password | High | Private subnet, secret manager, rotation |
| Wildcard IAM | High | Scope actions and resources |
| Privileged root pod with host root mount | High | Drop capabilities, non-root, narrow the mount |
| Unpinned base image | Low | Pin a version and digest |

## Stretch notes

- `checkov -d .` and `trivy config .` flag most of these. Compare their output with your list.
- A bucket policy with `Principal: "*"` plus `s3:GetObject` is another public path.
- A default-deny egress policy breaks the pod's ability to call the metadata service unless allowed.
- A non-root user needs a writable workdir and a numeric UID.
