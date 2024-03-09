from re import Pattern, compile


ConversionMapType = list[tuple[Pattern[str], str]]

NUMBER_CONMAP: ConversionMapType = [
    (compile(r"0"), "０"),
    (compile(r"1"), "１"),
    (compile(r"2"), "２"),
    (compile(r"3"), "３"),
    (compile(r"4"), "４"),
    (compile(r"5"), "５"),
    (compile(r"6"), "６"),
    (compile(r"7"), "７"),
    (compile(r"8"), "８"),
    (compile(r"9"), "９"),
]

CLEAN_CONMAP: ConversionMapType = [
    (compile(r"^.*[０-９]+版[０-９～－]*"), ""),
    (compile(r"[ \n]+$"), ""),
    (compile(r"◆$"), ""),
    (compile(r"【.+／.+】"), ""),
    (compile(r" {2,}"), " "),
]

SYMBOL_CONMAP: ConversionMapType = [
    (compile(r"—"), "－"),
    (compile(r"/"), "／"),
    (compile(r"︵"), "（"),
    (compile(r"︶"), "）"),
    (compile(r"︿"), "〈"),
    (compile(r"﹀"), "〉"),
    (compile(r"︽"), "《"),
    (compile(r"︾"), "》"),
    (compile(r"︻"), "【"),
    (compile(r"︼"), "】"),
    (compile(r"︗"), "〖"),
    (compile(r"︘"), "〗"),
    (compile(r"﹁"), "「"),
    (compile(r"﹂"), "」"),
    (compile(r"﹃"), "『"),
    (compile(r"﹄"), "』"),
    (compile(r"﹔"), "；"),
    (compile(r"﹕"), "："),
    (compile(r"﹖"), "？"),
    (compile(r"﹗"), "！"),
]

SPACE_CONMAP: ConversionMapType = [
    (compile(r"　"), " "),
    (compile(r"\r\n"), "\n"),
]


def convert_zht_text(text: str) -> str:
    """
    Converts the text in Tradition Chinese to a more readable format.

    The text orientation is horizontal.

    The line terminator is LF ("\n").
    """
    text = _convert_text(text, NUMBER_CONMAP)
    text = _convert_text(text, SPACE_CONMAP)
    text = _convert_text(text, SYMBOL_CONMAP)
    return text


def convert_data_to_lines(data: str) -> list[str]:
    """
    Converts the data into lines.

    The "data" refers to the `"Data"` or `"Hdr1"` attribute value in decoded packed data.
    """
    return [line.lstrip(" ") for line in clean_data(convert_zht_text(data)).split("\n")]


def clean_data(data: str) -> str:
    """
    Cleans any unnecessary character in the data.

    The "data" refers to the `"Data"` or `"Hdr1"` attribute value in decoded packed data.
    """
    return _convert_text(data, CLEAN_CONMAP)


def _convert_text(text: str, conmap: ConversionMapType) -> str:
    from re import sub

    for conversion in conmap:
        text = sub(*conversion, text)
    return text
