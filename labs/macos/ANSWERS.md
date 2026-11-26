# macOS lab answers

## 1. ATS

`NSAllowsArbitraryLoads` is true, so every host bypasses ATS. The `legacy.example` exception is redundant for clear text but documents the old host. Fix it with a narrow exception list or remove the global flag.

## 2. Entitlements

- `app-sandbox` is false, so no sandbox.
- `disable-library-validation` allows an unsigned dylib injection.
- `allow-dyld-environment-variables` allows `DYLD_INSERT_LIBRARIES`.
- `get-task-allow` allows debugger attach.
- `allow-jit` is normal for a JavaScript runtime but widens the memory path.

Fix it with the sandbox on and only the needed rights.

## 3. Launchd

The path is a user LaunchAgent. `RunAtLoad` and `KeepAlive` make it persistent. `/Users/Shared` is world writable on a default Mac, so any local user can replace `run.sh`.

## 4. Signing

`Signature=adhoc` and `TeamIdentifier=not set`, so the app is not signed by a team. `spctl` would reject it for distribution. A notarized build has a Developer ID and a ticket.

## 5. TCC

Full Disk Access is the highest. It reads Mail, Messages, browser profiles and every user file. Screen and microphone are next.

## 6. Secret

`APNS_TOKEN=mac-lab-7c1f` in the bundle. Revoke or rotate the token first, then rebuild, then check the old value.

## 7. Finding

Title. APNS token shipped in the app bundle.
Asset. `Sample.app/Contents/config.env`.
Impact. Any user who copies the app can push notifications as the app.
Fix. Move the token to the Keychain or a server, rotate the old value and add a build check.

## Chain

World writable launchd path plus no sandbox plus `disable-library-validation` is a local persistence and injection path. A local user replaces `run.sh`, waits for launchd, and runs in the user context with the app entitlements.
