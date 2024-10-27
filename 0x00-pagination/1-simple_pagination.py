#!/usr/bin/env python3
"""This function takes in two integer argument page and page_size
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This funtion takes the two integers and returns
       the start and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


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
        """This Function gets a page of data, indenx it
           and returns the list of rows for a specified page.
        """
        assert isinstance(page, int) and page > 0
        "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0
        "Page size must be a positive integer"
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index >= len(data):
            return []

        return data[start_index:end_index]
