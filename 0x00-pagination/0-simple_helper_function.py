#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function takes two arguments page and page_size and returns a tuple
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
