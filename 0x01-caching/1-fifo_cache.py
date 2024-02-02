#!/usr/bin/env python3
"""
class FIFOCache that inherits from BaseCaching and is a caching system
"""
from collections import deque
from typing import Any

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    Fifo Cache that inherits from BaseCaching
    """

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key: Any, item: Any) -> None:
        """
        Put an item in a cache using a FIFO mode
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = self.queue.popleft()
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """
        get an item in a cache using a FIFO
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
