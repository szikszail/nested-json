from io import StringIO
import json
from nested_json import load, loads, Nested


def test_loads():
    s = json.dumps({
        "id": "12345",
        "payload": json.dumps({
              "foo": "bar",
              "other": json.dumps([
                  "Hello", "World"
              ])
        })
    })
    assert loads(s) == {"id": "12345", "payload": Nested({
        "foo": "bar",
        "other": Nested([
            "Hello", "World"
        ])
    })}


def test_load():
    f = StringIO(json.dumps({
        "id": "12345",
        "payload": json.dumps({
              "foo": "bar",
              "other": json.dumps([
                  "Hello", "World"
              ])
        })
    }))
    assert load(f) == {"id": "12345", "payload": Nested({
        "foo": "bar",
        "other": Nested([
            "Hello", "World"
        ])
    })}
