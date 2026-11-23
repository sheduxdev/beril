---
description: Review Terraform, Kubernetes and Docker config
allowed-tools: Bash
---

Static review of local infrastructure config. No cloud API is called.

```bash
./beril infra --target "$ARGUMENTS" --out scans/infra
```

Read the line evidence. An absence check (no NetworkPolicy, no remote backend)
is a lead with low confidence, not a verdict.
