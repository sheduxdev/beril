# Android lab

A static manifest, network config, provider paths and strings. No device needed.

```bash
./tests.sh
```

| File | Question |
|---|---|
| `AndroidManifest.xml` | Exported components and flags |
| `network_security_config.xml` | Clear text scope |
| `file_paths.xml` | Provider path breadth |
| `strings.txt` | Endpoints, deep links and token |

## Tasks

1. List every exported component and say why it is or is not a risk.
2. Is the deep link verified? What can another app do with it?
3. Read the provider paths. What does `root-path /` expose?
4. Is the build debuggable and is the backup on?
5. Which hosts allow clear text and where is that set twice?
6. Find the token and name the revocation order.
7. Write the three fixes with the highest impact.

## Constraints

Static only. The APK is not built.

## Evidence

Quote the attribute and the file. An exported component without a caller is still a lead, not a bug.

Answers are in `ANSWERS.md`.
