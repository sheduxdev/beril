# Detection lab answers

## 1. Injection lines

Lines with `;id`, `%3Bcat /etc/passwd`, and `;wget ... | sh`.

## 2. False positive

A normal query with a semicolon, for example `?host=a;b`, fires the rule but may not be injection. Line 3 is the first true positive. A normal line with no semicolon is the negative control.

## 3. Specificity

`cs-uri-stem|endswith: diagnostic.cgi` and a semicolon in the query. Both are needed. A bare semicolon rule fires on every parameter with an encoded separator.

## 4. Extra field

`c-ip` for a known scanner range, or `sc-status: 200`, or a `cs-uri-query|contains: "/etc/passwd"` variant.

## 5. Matcher

```bash
python3 matcher.py --log access.log --rule rules/cgi_injection.yml
# hits=3
```

## 6. ATT&CK

`T1059.004`, Unix Shell. The rule already carries it.

## 7. False positive

`?host=127.0.0.1%3Becho%20ok` is a legitimate compound command in some deployments. If the app expects it, the rule still fires.

## 8. `wget` variant

```yaml
  selection_wget:
    cs-uri-query|contains: "wget"
  condition: selection or selection_wget
```

## 9. Scanner rule

```yaml
title: Known scanner user agent
detection:
  selection:
    cs-user-agent|contains:
      - "Nuclei"
      - "sqlmap"
      - "nikto"
```

## 10. Hit vs finding

A hit says "this pattern appeared". A finding says "this request reached a sink and changed behavior". The log alone cannot prove execution. The CGI response `uid=` does.

## Stretch notes

- Sigma conversion needs `sigma-cli` and a backend.
- A 200-only condition cuts 403 noise.
- A threshold catches brute force, not injection.
- Always measure false positives on a quiet day.
