#!/usr/bin/env python3
""" Simple helper function """


def index_range(page, page_size):
    """ return tuple with the first index and last index """
    start_index = (page * page_size) - page_size
    end_index = page * page_size
    return (start_index, end_index)
