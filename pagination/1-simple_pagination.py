#!/usr/bin/env python3
""" Simple helper function """
import csv
import math
from typing import List


def index_range(page, page_size):
    """ return tuple with the first index and last index """
    start_index = (page * page_size) - page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get data a this page """
        assert type(page) != str
        assert type(page_size) != str
        assert page > 0
        assert page_size > 0

        first_last_index = index_range(page, page_size)
        first_index = first_last_index[0]
        last_index = first_last_index[1]

        CSV = self.dataset()
        ROWPages = []

        for row in CSV[first_index:last_index]:
            ROWPages.append(row)
        return ROWPages
