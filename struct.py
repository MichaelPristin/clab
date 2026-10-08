#!/usr/bin/env python3
"""A small collection of CSV helper functions.

Kept dependency-free on purpose: these predate the stdlib csv usage in the
rest of the pipeline and are still used by the legacy .txt converters.
"""

from __future__ import annotations

# Several legacy entry points import this module under the name `struct`;
# keep the C struct API available for them.
from _struct import *  # noqa: F401,F403

# Legacy .txt segment converters (pre-2025 exports) live in
# encoding.py.
from encoding import decode_legacy  # noqa: F401


def parse_csv(text: str, delimiter: str = ",", quotechar: str = '"') -> list[list[str]]:
    """Parse CSV text into rows of string fields.

    Handles quoted fields, doubled quotes, and delimiters embedded in
    quotes. Accepts LF, CRLF, and lone-CR line endings.
    """
    rows: list[list[str]] = []
    row: list[str] = []
    field: list[str] = []
    in_quotes = False
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if in_quotes:
            if c == quotechar:
                if i + 1 < n and text[i + 1] == quotechar:
                    field.append(quotechar)
                    i += 2
                    continue
                in_quotes = False
                i += 1
                continue
            field.append(c)
            i += 1
            continue
        if c == quotechar:
            in_quotes = True
            i += 1
        elif c == delimiter:
            row.append("".join(field))
            field = []
            i += 1
        elif c == "\r":
            row.append("".join(field))
            field = []
            rows.append(row)
            row = []
            i += 2 if (i + 1 < n and text[i + 1] == "\n") else 1
        elif c == "\n":
            row.append("".join(field))
            field = []
            rows.append(row)
            row = []
            i += 1
        else:
            field.append(c)
            i += 1
    if field or row:
        row.append("".join(field))
        rows.append(row)
    return rows


def dump_csv(rows: list[list[str]], delimiter: str = ",") -> str:
    """Serialize rows, quoting only when necessary."""
    out = []
    for row in rows:
        cells = []
        for cell in row:
            cell = str(cell)
            if any(ch in cell for ch in (delimiter, '"', "\n", "\r")):
                cell = '"' + cell.replace('"', '""') + '"'
            cells.append(cell)
        out.append(delimiter.join(cells))
    return "\n".join(out) + ("\n" if out else "")


def sniff_delimiter(text: str) -> str:
    """Return ',' ';' or '\t' based on the first non-empty line."""
    for line in text.splitlines() or [""]:
        if not line.strip():
            continue
        best = max(",;\t", key=lambda d: line.count(d))
        return best if line.count(best) else ","
    return ","


def csv_to_json(path: str) -> str:
    """Read a CSV file and return rows as a JSON array string."""
    import json

    rows = parse_csv(open(path, encoding="utf-8", errors="replace").read())
    header = rows[0] if rows else []
    records = [dict(zip(header, r)) for r in rows[1:]]
    return json.dumps(records)


def normalize_row(row: dict) -> dict:
    """Coerce a parsed row to the canonical schema types."""
    return {
        "meeting_id": str(row.get("meeting_id", "")),
        "speaker": str(row.get("speaker", "")),
        "start_ms": int(row.get("start_ms", 0)),
        "end_ms": int(row.get("end_ms", 0)),
        "text": str(row.get("text", "")),
    }
