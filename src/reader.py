from typing import BinaryIO, ContextManager


class BinaryIOReader(ContextManager):
    """
    A convenient reader of `BinaryIO`
    """

    def __init__(self, input: BinaryIO, offset: int = 0) -> None:
        self._input = input
        self._offset = offset

    def read(self, size: int = -1) -> tuple[bytes, int]:
        """
        Reads `size` bytes and returns the chunk and the offset
        """
        offset = self._offset
        chunk = self._input.read(size)
        self._offset += len(chunk)
        return (chunk, offset)

    def __enter__(self):
        from io import BufferedIOBase, RawIOBase

        if not self._input.readable():
            raise OSError("expect a readable input")
        if not isinstance(self._input, (BufferedIOBase, RawIOBase)):
            raise OSError("expect a binary input")
        return self

    def __exit__(self, *args, **kwargs):
        return self._input.__exit__(*args, **kwargs)
