# nested-json

![PyPI](https://img.shields.io/pypi/v/nested-json?style=flat-square)

![PyPI - Downloads](https://img.shields.io/pypi/dw/nested-json?style=flat-square)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/szikszail/nested-json?style=flat-square)

## Install

```shell
pip install nested-json
```

## Usage

```python
import nested-json as njson
```

### Marking `dict` / `list` as nested

The `Nested` function can be used to mark a dictionary or
list as a nested data, which will add a special property to it, 
marking it nested. This property later removed during processing.

```python
data = {
  "id": "12345",
  "event": {
    "payload": {
      "rawpayload": njson.Nested({
        "key": "value",
        "other": 2,
        "foo": True
      }),
      "tags": njson.Nested([
        "hello",
        "world
      ])
    }
  }
}
# {
#   "id": "12345",
#   "event": {
#     "payload": {
#       "rawpayload": {
#         "__nested__": True,
#         "key": "value",
#         "other": 2,
#         "foo": True
#       },
#       "tags": [
#         "__nested__",
#         "hello",
#         "world
#       ]
#     }
#   }
# }
```

### Processing nested JSON

Using the `process` function, the nested keys can be removed
and nested data converted to JSON string.

```python
processed_data = njson.process(data)
# {
#   "id": "12345",
#   "event": {
#     "payload": {
#       "rawpayload": "{\"key\": \"value\", \"other\": 2, \"foo\": true}",
#       "tags": "[\"hello\", \"world\"]"
#     }
#   }
# }
```

### Converting to JSON string

The result of `process` can be already passed to `json.dumps` , 
but the `njson.dumps` can be also used with nested json data.

```python
json_string = njson.dumps(data)

# '{"id": "12345", "event": {"payload": {"rawpayload": "{\\"key\\": \\"value\\", \\"other\\": 2, \\"foo\\": true}", "tags": "[\\"hello\\", \\"world\\"]"}}}'
```

### Parsing JSON string

Nested JSON string can be parsed to nested json data with the `loads` function or the `parse` function

```python
assert njson.loads(json_string) == data
assert njson.parse(processed_data) == data
assert njson.parse(json.loads(json_string)) == data
```

## Compatibility

Note, that both `loads` and `dumps` uses the `json.loads` and `json.dumps` functions, thus they can be used with "normal" JSON as well.
