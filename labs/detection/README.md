# Detection lab

An access log with a command injection and a scanner. Write and test a rule.

```bash
./tests.sh
python3 matcher.py --log access.log --rule rules/cgi_injection.yml
```

The matcher supports two Sigma-like operators: `endswith` and `contains`.

## Tasks

1. Read the log. Which three requests are injection attempts?
2. Which line is a false positive for a generic "semicolon" rule?
3. Read the rule. Which fields make it specific?
4. Add one field that reduces noise further.
5. Run the matcher and record the three hits.
6. Map the technique to ATT&CK.
7. Write a false-positive case for the encoded semicolon.
8. Improve the rule to catch `wget` as well as `;`.
9. Write a second rule for scanner user agents.
10. Explain why a rule hit is not a finding.

## Evidence

Rule file, matcher output, and one paragraph on precision. A rule that fires on everything is not detection.

## Stretch

- Convert the rule to real Sigma and run it with `sigma convert`.
- Add a `status` condition for 200 only.
- Add a threshold for repeated attempts from one IP.
- Test against a normal day of logs and measure false positives.

Answers are in `ANSWERS.md`.
