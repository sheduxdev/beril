---
description: Verify ownership and run minimal active probes
allowed-tools: Bash
---

Active work needs a record. First check:

```bash
./beril verify --check "$ARGUMENTS"
```

If no record exists, issue a token and show the three publish paths:

```bash
./beril verify --new "$ARGUMENTS"
```

After the user publishes it and confirms, verify and scan:

```bash
./beril verify --verify "$ARGUMENTS"
./beril scan --target "https://$ARGUMENTS" --active --profile bugbounty --out scans/active
```

Never claim impact from a reflection alone. Read the false positive note.
