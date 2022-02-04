import json
from nested_json import parse


def test_parse_json_dict():
    assert parse(json.dumps({"foo": "bar"})) == {
        "__nested__": True,
        "foo": "bar"
    }


def test_parse_json_list():
    assert parse(json.dumps(["foo", "bar"])) == [
        "__nested__",
        "foo",
        "bar"
    ]


def test_parse_tuple():
    assert parse(("foo", "bar")) == ("foo", "bar")


def test_parse_list():
    assert parse(["foo", "bar"]) == ["foo", "bar"]


def test_parse_dict():
    assert parse({"foo": "bar"}) == {"foo": "bar"}


def test_parse_other_data():
    assert parse(1) == 1
    assert parse("Hello") == "Hello"
    assert parse(None) == None
    assert parse(True) == True
