class MarkerError(ValueError):
    """
    Indicates that none of the markers is found
    at the expected offset in the packed data
    """

    from .format import PackFormat

    def __init__(self, received, offset: int, *markers: PackFormat.Marker) -> None:
        """
        Indicates that none of `markers` matches `received`
        at the expected offset in the packed data
        """
        markers = [f"{m.name}: {m.value}" for m in markers[0]]
        if len(markers) <= 1:
            expected_name = "marker"
        else:
            expected_name = "one of the markers"
        expected_value = f"{{{', '.join(markers)}}}"
        super().__init__(
            f"expect {expected_name} {expected_value} at offset {offset} instead of {received}"
        )

    @staticmethod
    def check(received, offset: int, *markers: PackFormat.Marker) -> None:
        """
        Raises a MarkerError if none of `markers` matches `received`
        at the expected offset in the packed data
        """
        for marker in markers:
            if received != marker.value:
                raise MarkerError(received, offset, markers)
