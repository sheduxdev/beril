# Cloud lab

Static review of a small Terraform stack, a privileged pod, and a Dockerfile. No cloud account is required.

```bash
./tests.sh
```

## Tasks

1. Run `terraform validate` if Terraform is installed. What does it check, and what does it miss?
2. Read the S3 resource. What does `acl = "public-read"` expose?
3. Read the security group. Which ports are world-open, and which one is the larger risk?
4. Read the database. Why does `publicly_accessible = true` matter?
5. Read the IAM policy. What is the blast radius of `Action: "*"`?
6. Read the pod. Why are `privileged` and `runAsUser: 0` together worse than either alone?
7. The pod mounts host `/`. What can a shell in it read and write?
8. Read the Dockerfile. What is wrong with `node:latest`?
9. `API_KEY` is set with `ENV`. Is it a secret? What would be better?
10. Write three findings with a read-only proof and a fix.

## Evidence

Quote the line, name the exposed asset, and give the read-only command or console view. For a real account, `aws s3api get-bucket-acl` and `aws rds describe-db-instances` are enough.

## Stretch

- Run `checkov` or `trivy config .` against the directory.
- Add a bucket policy that blocks public access and compare.
- Add a network policy that denies egress.
- Rewrite the Dockerfile with a pinned digest and a non-root user.

Answers are in `ANSWERS.md`.
