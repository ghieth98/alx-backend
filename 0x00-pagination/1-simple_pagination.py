#!/usr/bin/env python3
"""
 method named get_page that takes two integer arguments page with default
 value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function takes two arguments page and page_size and returns a tuple
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """
    Server class to paginate a database of popular baby names.
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
        """
        This function takes two arguments page and page_size and returns a list
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start, end = index_range(page, page_size)

        data = self.dataset()

        return data[start:end] if end <= len(data) else data[start:]
