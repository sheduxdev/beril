# Crypto lab

Four broken primitives. Openssl CLI, local only.

```bash
python3 lab_server.py --port 8102
./tests.sh
```

| Endpoint | Bug |
|---|---|
| `/ecb` | ECB mode on controlled plaintext |
| `/cbc` | CBC with a fixed IV |
| `/padding` | Padding validity in the response |
| `/stream` | Caller chosen CTR nonce |
| `/hash` | MD5(secret + message) as a MAC |

## Tasks

1. Encrypt 32 identical bytes in ECB. Compare the blocks and explain the leak.
2. Take one CBC ciphertext and flip the last byte. Read the oracle.
3. Recover a plaintext block byte by byte with the oracle. Stop at one block.
4. Encrypt two different plaintexts with the same stream nonce. XOR the results.
5. Explain why the hash construction is not HMAC.
6. Write the fix for each endpoint.
7. Build one attack that recovers a secret through the oracle.

## Constraints

Local host. The key and the IV are fixed on purpose. No real data.

## Evidence

Keep the ciphertext, the request and the response. A padding oracle proof needs both a valid and an invalid pair.

## Stretch

- Turn the padding oracle into a full decrypt of a two block message.
- Add a MAC and show the order matters.
- Replace CTR with GCM and reuse the nonce.

Answers are in `ANSWERS.md`.
