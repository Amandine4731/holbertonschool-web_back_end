#!/usr/bin/env python3
""" type-annotated function which takes a list of int and float as argument
    and returns their sum as a float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return the sum of float and int. """
    return (sum(mxd_lst))
