# Tools for Slash-Hash Packed Data Format

[![PyPI](https://img.shields.io/pypi/pyversions/shpdf-tools?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/shpdf-tools/)

## User guide

### 1. Obtain some data

- The packed data contains some unreadable characters
- The packed data should be encoded in `big5` or `cp950`
- The packed data extension does not matter
- The packed data should look like this (in cp950 encoding)

```plaintext
?坼#ADte   101662/06/23\#AuID    10\#AuNm    6鄭成功\#ArID    10\#VerN    10\#Hdr1   24０版～１～鄭成功，在台灣\#Hdr2    0\#Hdr3    0\#ALno    12\#Word    228\#PbID    0?怕K?B
０版～１～鄭成功，在台灣
　︻記者鄭成功／報導︼▓︵國姓爺︶。◆
?
```

### 2. Install our tools

- Using `pip`

  ```shell
  pip install shpdf-tools
  ```

- Using `poetry`

  ```shell
  poetry add shpdf-tools
  ```

### 3. Use our tools to process the packed data

- Decode and encode the packed data

  ```python
  from shpdf_tools.decode import decode_dict
  from shpdf_tools.encode import encode_json
  from io import BytesIO

  packed_data = b'\xc8\xa9\\#ADte   101662/06/23\\#AuID    10\\#AuNm    6\xbeG\xa6\xa8\xa5\\\\#ArID    10\\#VerN    10\\#Hdr1   24\xa2\xaf\xaa\xa9\xa1\xe3\xa2\xb0\xa1\xe3\xbeG\xa6\xa8\xa5\\\xa1A\xa6b\xa5x\xc6W\\#Hdr2    0\\#Hdr3    0\\#ALno    12\\#Word    228\\#PbID    0\xc8\xa9\xc8K\xc8B\r\n\xa2\xaf\xaa\xa9\xa1\xe3\xa2\xb0\xa1\xe3\xbeG\xa6\xa8\xa5\\\xa1A\xa6b\xa5x\xc6W\r\n\xa1@\xa1k\xb0O\xaa\xcc\xbeG\xa6\xa8\xa5\\\xa1\xfe\xb3\xf8\xbe\xc9\xa1l\xf9\xfe\xa1_\xb0\xea\xa9m\xb7\xdd\xa1`\xa1C\xa1\xbb\r\n\x00'

  decoded_packed_data = decode_dict(BytesIO(packed_data))

  # Check the decoded data
  assert decoded_packed_data['ADte'] == '1662/06/23'
  assert decoded_packed_data['PbID'] == ''
  assert decoded_packed_data['Data'] == '０版～１～鄭成功，在台灣\r\n\u3000︻記者鄭成功／報導︼▓︵國姓爺︶。◆\r\n'

  # Encode the decoded data
  encoded_packed_data = encode_json(decoded_packed_data)

  # Check the encoded data
  assert encoded_packed_data != b''
  ```
