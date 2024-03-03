# Tools for Slash-Hash Packed Data Format

[![PyPI](https://img.shields.io/pypi/pyversions/shpdf-tools?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/shpdf-tools/)

## Introduction

Slash-Hash Packed Data Format (SHPDF) is a legacy data format. The original data and specification is missing. This project aims to provide tools to process SHPDF data. Please note that our implementation is based on personal conjuncture and may not be accurate.

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
  assert encoded_packed_data == b'{"ADte":"1662/06/23","AuID":"0","AuNm":"\xe9\x84\xad\xe6\x88\x90\xe5\x8a\x9f","ArID":"0","VerN":"0","Hdr1":"\xef\xbc\x90\xe7\x89\x88\xef\xbd\x9e\xef\xbc\x91\xef\xbd\x9e\xe9\x84\xad\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x8c\xe5\x9c\xa8\xe5\x8f\xb0\xe7\x81\xa3","Hdr2":"","Hdr3":"","ALno":"2","Word":"28","PbID":"","Data":"\xef\xbc\x90\xe7\x89\x88\xef\xbd\x9e\xef\xbc\x91\xef\xbd\x9e\xe9\x84\xad\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x8c\xe5\x9c\xa8\xe5\x8f\xb0\xe7\x81\xa3\\r\\n\xe3\x80\x80\xef\xb8\xbb\xe8\xa8\x98\xe8\x80\x85\xe9\x84\xad\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x8f\xe5\xa0\xb1\xe5\xb0\x8e\xef\xb8\xbc\xe2\x96\x93\xef\xb8\xb5\xe5\x9c\x8b\xe5\xa7\x93\xe7\x88\xba\xef\xb8\xb6\xe3\x80\x82\xe2\x97\x86\\r\\n"}'
  ```

## License

- [MIT License](./LICENSE)
