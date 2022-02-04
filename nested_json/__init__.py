import json
import re
from typing import Any

__NESTED__ = "__nested__"


def Nested(obj: Any, in_place: bool = True) -> Any:
    if type(obj) is dict:
        if not in_place:
            obj = obj.copy()
        obj[__NESTED__] = True
    elif type(obj) is list:
        if not in_place:
            obj = obj.copy()
        obj.insert(0, __NESTED__)
    return obj


def _is_json_string(s: str) -> bool:
    p = re.compile(r'^(?:\{.*\}|\[.*\])$')
    return bool(p.match(s))


def loads(s: str, **kwargs) -> Any:
    return parse(json.loads(s, **kwargs))


def parse(obj: Any) -> Any:
    if type(obj) is str and _is_json_string(obj):
        return Nested(loads(obj))
    if type(obj) is dict:
        return {k: parse(v) for k, v in obj.items()}
    if type(obj) is list:
        return [parse(i) for i in obj]
    if type(obj) is tuple:
        return tuple(parse(i) for i in obj)
    return obj


def process(obj: Any) -> Any:
    if type(obj) is list:
        if __NESTED__ not in obj:
            return [process(i) for i in obj]
        obj.remove(__NESTED__)
        return json.dumps(process(obj))
    if type(obj) is dict:
        if __NESTED__ not in obj:
            return {k: process(v) for k, v in obj.items()}
        obj.pop(__NESTED__)
        return json.dumps(process(obj))
    if type(obj) is tuple:
        return tuple(process(i) for i in obj)
    return obj


def dumps(obj: Any, **kwargs) -> str:
    return json.dumps(process(obj), **kwargs)
