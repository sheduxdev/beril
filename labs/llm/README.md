# LLM lab

A support agent with RAG and tools. The transcripts are fixtures, not a live model. Use them to practice impact writing.

```bash
./tests.sh
```

Read `app_spec.md` and the four transcripts.

## Tasks

1. Map the trust boundary: system prompt, user input, retrieved chunk, tool output.
2. Which transcript is direct injection, and what leaked?
3. Which is indirect injection, and how did the payload arrive?
4. Which is an exfiltration channel, and why does Markdown help?
5. Which is cross-user leakage, and where is the missing filter?
6. `read_file` has no root. Which paths would you try first?
7. `send_email` can leave the tenant. What data would you send?
8. Rank the four by impact. Which needs a user action?
9. Write fixes for the retriever, the file tool, and the renderer.
10. Write one report with a reproducible prompt and the observed output.

## Evidence

Keep the exact prompt, the retrieved source, and the output. Label a model behavior as confirmed only when you ran it.

## Stretch

- Build a tiny RAG with two users and a shared doc.
- Add an allowlist to `read_file` and rerun the traversal prompt.
- Add a Markdown image proxy and strip remote images.
- Test a tool-call confusion: make the model call `send_email` with an attacker address.

Answers are in `ANSWERS.md`.
