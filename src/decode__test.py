from .decode import decode_dict, decode_list
from pathlib import Path


def test_simple_decode_dict_has_data():
    for path in Path("dataset/simple").glob("**/*"):
        data = decode_dict(path.open("rb")).get("Data")
        assert data is not None


def test_simple_decode_list_has_length():
    for path in Path("dataset/simple").glob("**/*"):
        decoded = decode_list(path.open("rb"))
        assert len(decoded) > 0
