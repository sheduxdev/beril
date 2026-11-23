---
description: Container image scan through Trivy, Grype and Syft
allowed-tools: Bash
---

Use installed tools only. Prefer a local tar when the registry is slow.

```bash
./beril image --target "$ARGUMENTS" --out scans/image
```

The SBOM is written when Syft exists. A missing tool is named in the report.
