#!/usr/bin/env python3
""" type-annotated function which takes a float as argument
    and returns the float multiplied.
"""


from typing import Callable


def make_multiplier(multiplier: float, x: float) -> Callable[[float], float]:
    """ return the float multiplied. """

    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
