#!/usr/bin/env python3
"""
This module implements the LruCache method
"""

from collections import OrderedDict
from typing import Any

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    This class implements the LRU caching
    """

    def __init__(self):
        """
        Initialize the LRU caching class
        """
        super().__init__()
        self.queue = OrderedDict()

    def put(self, key: Any, item: Any) -> None:
        """
        Add a new item to the LRU cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.move_to_end(key)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key, _ = self.queue.popitem(last=False)
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))

            self.queue[key] = None
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """
        Get an item from the LRU cache
        """
        if key is not None and key in self.cache_data:
            self.queue.move_to_end(key)
            return self.cache_data[key]
        return None
