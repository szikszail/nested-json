import json
from nested_json import dumps, Nested


def test_dumps():
    data = {"id": "12345", "payload": Nested({
        "foo": "bar",
        "other": Nested([
            "Hello", "World"
        ])
    })}
    assert dumps(data, indent="--") == json.dumps({
        "id": "12345",
        "payload": json.dumps({
            "foo": "bar",
            "other": json.dumps([
                "Hello", "World"
            ])
        })
    }, indent='--')
