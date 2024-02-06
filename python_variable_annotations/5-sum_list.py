#!/usr/bin/env python3
""" type-annotated function which takes a list of floats as argument
    and returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ return the sum of floats. """
    return (sum(input_list))
