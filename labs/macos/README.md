# macOS lab

A static app bundle and host artifacts. No Mac needed for the reading pass.

```bash
./tests.sh
```

| File | Question |
|---|---|
| `Sample.app/Contents/Info.plist` | ATS exception scope and version |
| `Sample.app/Contents/entitlements.plist` | Which hardening right is open |
| `launchd/com.example.agent.plist` | Persistence and the writable path |
| `codesign.txt` | Signing identity and team |
| `tcc.txt` | Privacy grants and the blast radius |
| `Sample.app/Contents/config.env` | Secret in the bundle |

## Tasks

1. Read the ATS block. Which hosts are covered by the arbitrary load?
2. List every entitlement that widens the attack surface.
3. Is the launchd job a user agent or a daemon? What path does it run and who can write it?
4. Is the app notarized? What does the team field say?
5. Which TCC grant is the highest impact and why?
6. Name the secret in the bundle and the revocation order.
7. Write one finding with a fix and an evidence path.

## Constraints

Static only. The bundle is not signed and does not run.

## Evidence

Quote the key line and the file path. A task without a key is an opinion.

Answers are in `ANSWERS.md`.
