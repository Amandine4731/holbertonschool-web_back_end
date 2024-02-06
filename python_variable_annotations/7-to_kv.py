#!/usr/bin/env python3
""" type-annotated function which takes a str and int or float as argument
    and returns a tuple.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return the sum of float and int. """
    return (k, v**2)
