# Android lab answers

## 1. Exported components

- `MainActivity` is the launcher and is normally exported. It also takes the `sample://open` link.
- `WebViewActivity` is exported and takes `sample://web?url=`. It is the highest interest, a URL from any app reaches a WebView.
- `BootReceiver` is exported but only reacts to the system broadcast.
- The FileProvider is exported with URI grants. The authority is fixed.

`SyncService` is private.

## 2. Deep link

`autoVerify=false` and the scheme is custom, so any app can register `sample://` and receive the link, or send one. The WebView activity trusts a `url` value.

## 3. Provider paths

`root-path name="root" path="/"` exposes the whole filesystem through the provider, not only the app files. `external-path .` exposes all external storage. Fix it with narrower paths.

## 4. Build flags

`debuggable=true` allows `run-as` and a debugger. `allowBackup=true` allows an adb or cloud backup of app data. Both are release risks.

## 5. Clear text

`usesCleartextTraffic=true` covers all hosts. `network_security_config` repeats it in the base config and for `legacy.example`. The base flag is redundant and hides the narrower intent. Fix it by removing the global flag and keeping the domain exception.

## 6. Token

`API_TOKEN=android-lab-3d9e` in `strings.txt`. Revoke the token at the API, rotate it, ship a build, then remove the old string.

## 7. Fixes

1. Set `autoVerify=true` with an https App Link and validate the `url` in the WebView.
2. Disable cleartext or narrow it to the one legacy host.
3. Turn off backup and debuggable for release, and narrow the provider paths.

## Chain

A malicious app sends `sample://web?url=https://evil.example` to the exported activity. The WebView loads the page with the bridge if one is registered, and the page reaches native methods.
