from __future__ import annotations


def encode_json(decoded: list[tuple[str, str]] | dict[str, str]) -> bytes:
    """
    Encodes the decoded packed data into JSON format
    """
    from msgspec.json import encode

    return encode(dict(decoded))
