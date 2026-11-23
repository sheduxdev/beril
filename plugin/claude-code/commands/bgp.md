---
description: Passive BGP and RPKI posture for a prefix or ASN
allowed-tools: Bash
---

Passive lookup only. Nothing is announced.

```bash
./beril bgp --prefix "$ARGUMENTS"
```

Read the RPKI state and the visibility. Confirm a suspected hijack on two
collectors before contacting a NOC. `docs/bgp-runbook.md` is the incident path.
