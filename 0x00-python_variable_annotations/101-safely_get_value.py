#!/usr/bin/env python3
''' task 11 '''
from typing import TypeVar, Union, Mapping, Any

T = TypeVar("T")
Def = Union[T, None]
result = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> result:
    """Type Var annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
