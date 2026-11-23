#!/usr/bin/env python3
"""Structural validation of a SARIF 2.1.0 document.

The official schema is JSON Schema. Adding ``jsonschema`` as a dependency for
one output would be heavy, so this module checks the parts Beril emits and the
parts a consumer relies on: version, tool driver, rule ids, level enums,
message, locations, fingerprints and invocation timestamps. It is not a full
JSON Schema validator and says so.

    from sarif_schema import validate
    errors = validate(document)
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
from typing import Any

SCHEMA_URL = "https://json.schemastore.org/sarif-2.1.0.json"
SCHEMA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references", "sarif-2.1.0.schema.json"
)
LEVELS = {"none", "note", "warning", "error"}
URI_RE = re.compile(r"^[a-z][a-z0-9+.-]*://", re.I)
_SCHEMA: dict | None = None


def _rfc3339(value: Any) -> bool:
    if not isinstance(value, str) or len(value) < 20:
        return False
    try:
        dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return "T" in value


def validate(doc: Any) -> list[str]:
    """Return a list of schema violations. Empty means structurally valid.

    Args:
        doc: Parsed SARIF document.

    Returns:
        Human readable error strings.
    """
    errors: list[str] = []

    def fail(path: str, message: str) -> None:
        errors.append(f"{path}: {message}")

    if not isinstance(doc, dict):
        return ["$: document must be an object"]
    if doc.get("$schema") and doc["$schema"] != SCHEMA_URL:
        fail("$schema", f"expected {SCHEMA_URL}")
    if doc.get("version") != "2.1.0":
        fail("version", "must be the string 2.1.0")
    runs = doc.get("runs")
    if not isinstance(runs, list) or not runs:
        return [*errors, "runs: must be a non-empty array"]
    for index, run in enumerate(runs):
        prefix = f"runs[{index}]"
        if not isinstance(run, dict):
            fail(prefix, "must be an object")
            continue
        tool = run.get("tool")
        driver = tool.get("driver") if isinstance(tool, dict) else None
        if not isinstance(driver, dict):
            fail(prefix + ".tool.driver", "required object")
            driver = {}
        if not isinstance(driver.get("name"), str) or not driver.get("name"):
            fail(prefix + ".tool.driver.name", "required non-empty string")
        rules = driver.get("rules", [])
        rule_ids: set[str] = set()
        if not isinstance(rules, list):
            fail(prefix + ".tool.driver.rules", "must be an array")
            rules = []
        for r_index, rule in enumerate(rules):
            r_prefix = f"{prefix}.tool.driver.rules[{r_index}]"
            if not isinstance(rule, dict):
                fail(r_prefix, "must be an object")
                continue
            rule_id = rule.get("id")
            if not isinstance(rule_id, str) or not rule_id:
                fail(r_prefix + ".id", "required non-empty string")
            elif rule_id in rule_ids:
                fail(r_prefix + ".id", f"duplicate rule id {rule_id}")
            else:
                rule_ids.add(rule_id)
            for field in ("shortDescription", "fullDescription"):
                text = (rule.get(field) or {}).get("text") if isinstance(rule.get(field), dict) else None
                if not isinstance(text, str) or not text:
                    fail(f"{r_prefix}.{field}.text", "required non-empty string")
            level = (rule.get("defaultConfiguration") or {}).get("level")
            if level is not None and level not in LEVELS:
                fail(r_prefix + ".defaultConfiguration.level", f"unknown level {level}")
        automation = run.get("automationDetails")
        if automation is not None and not isinstance((automation or {}).get("id"), str):
            fail(prefix + ".automationDetails.id", "must be a string")
        results = run.get("results", [])
        if not isinstance(results, list):
            fail(prefix + ".results", "must be an array")
            results = []
        for s_index, result in enumerate(results):
            s_prefix = f"{prefix}.results[{s_index}]"
            if not isinstance(result, dict):
                fail(s_prefix, "must be an object")
                continue
            rule_id = result.get("ruleId")
            rule_index = result.get("ruleIndex")
            if rule_id is None and rule_index is None:
                fail(s_prefix, "ruleId or ruleIndex required")
            if rule_id is not None and rule_id not in rule_ids:
                fail(s_prefix + ".ruleId", f"unknown rule {rule_id}")
            if rule_index is not None and (not isinstance(rule_index, int) or not 0 <= rule_index < len(rules)):
                fail(s_prefix + ".ruleIndex", "out of range")
            message = (result.get("message") or {}).get("text") if isinstance(result.get("message"), dict) else None
            if not isinstance(message, str) or not message:
                fail(s_prefix + ".message.text", "required non-empty string")
            if result.get("level") not in LEVELS:
                fail(s_prefix + ".level", f"unknown level {result.get('level')}")
            locations = result.get("locations")
            if locations is not None:
                if not isinstance(locations, list):
                    fail(s_prefix + ".locations", "must be an array")
                else:
                    for l_index, location in enumerate(locations):
                        physical = (location or {}).get("physicalLocation") if isinstance(location, dict) else None
                        if not isinstance(physical, dict):
                            fail(f"{s_prefix}.locations[{l_index}].physicalLocation", "required object")
                            continue
                        uri = (physical.get("artifactLocation") or {}).get("uri")
                        if uri is not None and not isinstance(uri, str):
                            fail(
                                f"{s_prefix}.locations[{l_index}].physicalLocation.artifactLocation.uri",
                                "must be a string",
                            )
                        region = physical.get("region")
                        if region is not None and (
                            not isinstance(region, dict) or not isinstance(region.get("startLine"), int)
                        ):
                            fail(
                                f"{s_prefix}.locations[{l_index}].physicalLocation.region.startLine", "required integer"
                            )
            fingerprints = result.get("partialFingerprints")
            if fingerprints is not None:
                if not isinstance(fingerprints, dict):
                    fail(s_prefix + ".partialFingerprints", "must be an object")
                elif not all(isinstance(k, str) and isinstance(v, str) for k, v in fingerprints.items()):
                    fail(s_prefix + ".partialFingerprints", "keys and values must be strings")
        invocations = run.get("invocations")
        if invocations is not None:
            if not isinstance(invocations, list):
                fail(prefix + ".invocations", "must be an array")
            else:
                for i_index, invocation in enumerate(invocations):
                    i_prefix = f"{prefix}.invocations[{i_index}]"
                    if not isinstance(invocation, dict):
                        fail(i_prefix, "must be an object")
                        continue
                    if not isinstance(invocation.get("executionSuccessful"), bool):
                        fail(i_prefix + ".executionSuccessful", "required boolean")
                    for field in ("startTimeUtc", "endTimeUtc"):
                        if field in invocation and not _rfc3339(invocation[field]):
                            fail(f"{i_prefix}.{field}", "must be an RFC 3339 timestamp")
                    for n_index, note in enumerate(invocation.get("toolExecutionNotifications") or []):
                        text = (note or {}).get("message", {}).get("text") if isinstance(note, dict) else None
                        if not isinstance(text, str) or not text:
                            fail(
                                f"{i_prefix}.toolExecutionNotifications[{n_index}].message.text",
                                "required non-empty string",
                            )
    return errors


def official_errors(doc: Any) -> list[str]:
    """Validate against the vendored official schema when ``jsonschema`` exists.

    Args:
        doc: Parsed SARIF document.

    Returns:
        Error strings, or an empty list when the library or schema is absent.
    """
    global _SCHEMA
    try:
        import jsonschema
    except ImportError:
        return []
    if _SCHEMA is None:
        try:
            with open(SCHEMA_FILE, encoding="utf-8") as handle:
                _SCHEMA = json.load(handle)
        except (OSError, json.JSONDecodeError):
            return []
    schema = _SCHEMA
    if schema is None:
        return []
    validator = jsonschema.Draft7Validator(schema)
    return [f"{'/'.join(str(part) for part in error.path)}: {error.message}" for error in validator.iter_errors(doc)]


def ensure(doc: Any) -> None:
    """Raise ``ValueError`` when the document is invalid.

    Runs the structural checks always and the official schema when
    ``jsonschema`` is installed.

    Args:
        doc: Parsed SARIF document.
    """
    errors = validate(doc) + official_errors(doc)
    if errors:
        raise ValueError("invalid SARIF: " + "; ".join(errors[:10]))


def valid_uri(value: str) -> bool:
    """True when a string looks like an absolute URI."""
    return bool(URI_RE.match(value or ""))
