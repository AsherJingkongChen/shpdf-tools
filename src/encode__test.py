from msgspec import json
from pathlib import Path

from .decode import decode_dict, decode_list
from .encode import encode_json


def test_simple_encode_reencodable():
    for path in Path("dataset/simple").glob("**/*"):
        decoded = decode_dict(path.open("rb"))
        encoded = encode_json(decoded)
        redecoded = json.decode(encoded)
        reencoded = json.encode(redecoded)
        assert encoded == reencoded


def test_simple_encode_accepts_dict_and_list():
    for path in Path("dataset/simple").glob("**/*"):
        decoded_dict = decode_dict(path.open("rb"))
        decoded_list = decode_list(path.open("rb"))
        encoded_dict = encode_json(decoded_dict)
        encoded_list = encode_json(decoded_list)
        assert encoded_dict == encoded_list
