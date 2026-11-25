# Crypto lab answers

## 1. ECB block equality

```bash
curl -s --get --data-urlencode 'data=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' 'http://127.0.0.1:8102/ecb'
```

The first two 16 byte blocks are equal. ECB encrypts each block independently. The fix is CBC, CTR or GCM with a random IV or nonce.

## 2. Padding oracle

```bash
CBC=$(curl -s --get --data-urlencode 'data=AAAAAAAAAAAAAAAA' 'http://127.0.0.1:8102/cbc')
IV=${CBC%%:*}
CT=${CBC##*:}
curl -s --get --data-urlencode "data=$IV$CT" 'http://127.0.0.1:8102/padding'
curl -s --get --data-urlencode "data=$IV${CT:0:30}00" 'http://127.0.0.1:8102/padding'
```

The first returns valid and the second invalid. The fix is a single uniform error or an encrypt then MAC construction.

## 3. Byte by byte

The last plaintext byte is controlled by the last ciphertext byte of the previous block, which is the IV for the first block. Flip the IV byte until the response is valid. The value is `0x01 XOR the flipped byte`. Then set the last byte to `0x02` and repeat for the second last. One block is enough for the exercise.

## 4. Stream nonce reuse

```bash
NONCE=0102030405060708090a0b0c0d0e0f10
A=$(curl -s --get --data-urlencode 'data=AAAAAAAAAAAAAAAA' --data-urlencode "nonce=$NONCE" 'http://127.0.0.1:8102/stream')
B=$(curl -s --get --data-urlencode 'data=BBBBBBBBBBBBBBBB' --data-urlencode "nonce=$NONCE" 'http://127.0.0.1:8102/stream')
python3 -c "a=bytes.fromhex('$A');b=bytes.fromhex('$B');print(bytes(x^y for x,y in zip(a,b)).hex())"
```

The XOR is `03` repeated. The keystream cancels. The fix is a random or counter nonce per message.

## 5. Why not HMAC

`md5(secret + data)` is vulnerable to length extension. An attacker who knows the secret length can append data and compute a valid digest. HMAC is not.

## 6. Fixes

- ECB to GCM or CBC with a random IV.
- Uniform error and encrypt then MAC.
- Random 96 bit nonce per message.
- HMAC-SHA256 or a keyed BLAKE2.

## 7. Full attack

Decrypt one block through the oracle, or recover a token by flipping the IV. Report the request pairs, the recovered bytes and the fix.

## Stretch notes

A MAC before encryption leaks padding and allows a bit flip with a valid MAC in some cases. Encrypt then MAC is the safer order. GCM nonce reuse leaks the authentication key as well as the plaintext.
