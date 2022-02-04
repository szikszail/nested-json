import json
from nested_json import Nested, process


def test_process_nested_dict():
    data = {"foo": "bar"}
    assert process(Nested(data)) == json.dumps(data)


def test_process_non_nested_dict():
    data = {"foo": "bar"}
    assert process(data) == data


def test_process_multilevel_dict():
    data = {"id": "12345", "payload": Nested({
        "foo": "bar",
        "other": Nested({
            "hello": "world"
        })
    })}
    assert process(data) == {
        "id": "12345",
        "payload": json.dumps({
            "foo": "bar",
            "other": json.dumps({
                "hello": "world"
            })
        })
    }


def test_process_nested_list():
    data = ["foo", "bar"]
    assert process(Nested(data)) == json.dumps(data)


def test_process_non_nested_list():
    data = ["foo", "bar"]
    assert process(data) == data


def test_process_multilevel_list():
    data = ["foo", Nested(["hello", "world", Nested(["other"])])]
    assert process(data) == [
        "foo",
        json.dumps([
            "hello",
            "world",
            json.dumps(["other"])
        ])
    ]


def test_process_mixed():
    data = {"id": "12345", "payload": Nested({
        "foo": "bar",
        "other": Nested([
            "Hello", "World"
        ])
    })}
    assert process(data) == {
        "id": "12345",
        "payload": json.dumps({
            "foo": "bar",
            "other": json.dumps([
                "Hello", "World"
            ])
        })
    }


def test_process_tuple_with_nested_json():
    assert process((1, Nested([1, 2]), 2)) == (1, json.dumps([1, 2]), 2)


def test_process_other_data():
    assert process(1) == 1
    assert process("Hello") == "Hello"
    assert process({1, 2}) == {1, 2}
    assert process((1, 2)) == (1, 2)
    assert process(True) == True
    assert process(None) == None
