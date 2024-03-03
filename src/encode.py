from typing import Union


def encode_json(decoded: Union[list[tuple[str, str]], dict[str, str]]) -> bytes:
    """
    Encodes the decoded packed data into JSON format
    """
    from msgspec.json import encode

    return encode(dict(decoded))
