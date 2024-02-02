#!/usr/bin/env python3
"""
This module implements the lifo caching mechanism
"""
from collections import deque
from typing import Any

BaseCaching = __import__("base_caching").BaseCaching


class LifoCache(BaseCaching):
    """
    This class implements the lifo caching
    """

    def __init__(self):
        """
        Initialize the lifo caching class
        """
        super().__init__()
        self.queue = deque()

    def put(self, key: Any, item: Any) -> None:
        """
        Add a new item to the lifo cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)

            elif len(self.cache_data) <= BaseCaching.MAX_ITEMS:
                discard_key = self.queue.pop()
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """
        Get an item from the lifo cache
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
