class PackFormat:
    """
    Specifications of the Slash-Hash Packed Data Format.
    """

    from enum import Enum

    class Length(Enum):
        START_MARKER = 2
        ATTR_KEY = 4
        ATTR_VALUE_SIZE = 5
        DATA_START_MARKER = 6
        FORM_END_MARKER = 1

    class Marker(Enum):
        FORM_START = b"\xC8\xA9"
        ATTR_START = b"\x5C\x23"
        WHITE_SPACE = b"\x20"
        DATA_START = b"\xC8\x4B\xC8\x42\x0D\x0A"
        FORM_END = b"\x00"

    class Text(Enum):
        ENCODING = "cp950"
