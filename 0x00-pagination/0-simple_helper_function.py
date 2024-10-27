#!/usr/bin/env python3
"""This function takes in two integer argument page and page_size
"""


def index_range(page: int, page_size: int) -> tuple:
    """This funtion takes the two integers and returns
       the start and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
