from nested_json import Nested


def test_nested_with_dict():
    assert Nested({
        "foo": "bar"
    }) == {
        "__nested__": True, "foo": "bar"
    }


def test_nested_with_list():
    assert Nested([
        "hello", "world"
    ]) == [
        "__nested__", "hello", "world"
    ]


def test_nested_other_value():
    assert Nested("Hello") == "Hello"
    assert Nested(None) == None


def test_nested_dict_inplace():
    data = {"foo": "bar"}
    nested = Nested(data)
    assert nested == data == {"__nested__": True, "foo": "bar"}


def test_nested_dict_not_inplace():
    data = {"foo": "bar"}
    nested = Nested(data, in_place=False)
    assert data != nested
    assert nested == {"__nested__": True, "foo": "bar"}


def test_nested_list_inplace():
    data = ["foo", "bar"]
    nested = Nested(data)
    assert nested == data == ["__nested__", "foo", "bar"]


def test_nested_list_not_inplace():
    data = ["foo", "bar"]
    nested = Nested(data, in_place=False)
    assert data != nested
    assert nested == ["__nested__", "foo", "bar"]
