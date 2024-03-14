from typing import BinaryIO, Generator

from .error import MarkerError
from .format import PackFormat
from .reader import BinaryIOReader


def decode_dict(input: BinaryIO) -> dict[str, str]:
    """
    Decodes the packed data stream into a dictionary
    """
    return dict(_decode(input))


def decode_list(input: BinaryIO) -> list[tuple[str, str]]:
    """
    Decodes the packed data stream into a key-value pair list
    """
    return list(_decode(input))


def _decode(input: BinaryIO) -> Generator[tuple[str, str], None, None]:
    with BinaryIOReader(input) as reader:
        chunk, offset = reader.read(PackFormat.Length.START_MARKER.value)
        MarkerError.check(chunk, offset, PackFormat.Marker.FORM_START)
        while True:
            chunk, offset = reader.read(PackFormat.Length.START_MARKER.value)
            if chunk == PackFormat.Marker.ATTR_START.value:
                yield _decode_attr(reader)
            elif chunk == PackFormat.Marker.FORM_START.value:
                yield ("Data", _decode_data(reader))
                break
            else:
                raise MarkerError(
                    chunk,
                    offset,
                    PackFormat.Marker.ATTR_START,
                    PackFormat.Marker.FORM_START,
                )


def _decode_attr(reader: BinaryIOReader) -> tuple[str, str]:
    chunk = reader.read(PackFormat.Length.ATTR_KEY.value)[0]
    attr_key = chunk.decode(PackFormat.Text.ENCODING.value, "ignore")
    chunk = reader.read(PackFormat.Length.ATTR_VALUE_SIZE.value)[0]
    attr_value_size = int(
        chunk.lstrip(PackFormat.Marker.WHITE_SPACE.value).decode(
            PackFormat.Text.ENCODING.value, "ignore"
        )
    )
    chunk = reader.read(attr_value_size)[0]
    attr_value = chunk.decode(PackFormat.Text.ENCODING.value, "ignore")
    return (attr_key, attr_value)


def _decode_data(reader: BinaryIOReader) -> str:
    chunk, offset = reader.read(PackFormat.Length.DATA_START_MARKER.value)
    MarkerError.check(chunk, offset, PackFormat.Marker.DATA_START)
    remain, offset = reader.read()
    offset -= PackFormat.Length.FORM_END_MARKER.value
    chunk = remain[-PackFormat.Length.FORM_END_MARKER.value :]
    # MarkerError.check(chunk, offset, PackFormat.Marker.FORM_END)
    chunk = remain[: -PackFormat.Length.FORM_END_MARKER.value]
    data = chunk.decode(PackFormat.Text.ENCODING.value, "ignore")
    return data
