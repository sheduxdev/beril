"""Small file helpers with explicit encodings and context managers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_text(path: str | Path, limit: int | None = None) -> str:
    """Read a UTF-8 text file.

    Args:
        path: File path.
        limit: Maximum bytes to read, or None for the whole file.

    Returns:
        The decoded text.

    Raises:
        OSError: When the file cannot be read.
    """
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read(limit) if limit else handle.read()


def write_text(path: str | Path, text: str) -> None:
    """Write UTF-8 text and create parent directories.

    Args:
        path: Destination path.
        text: Content to write.
    """
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)


def load_json(path: str | Path, default: Any = None) -> Any:
    """Load JSON, returning a default on read or parse failure.

    Args:
        path: File path.
        default: Value returned on failure.

    Returns:
        Parsed data or the default.
    """
    try:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return default


def write_json(path: str | Path, payload: Any, indent: int = 2) -> None:
    """Write JSON with a trailing newline.

    Args:
        path: Destination path.
        payload: JSON serialisable data.
        indent: Indentation width.
    """
    write_text(path, json.dumps(payload, ensure_ascii=False, indent=indent) + "\n")
