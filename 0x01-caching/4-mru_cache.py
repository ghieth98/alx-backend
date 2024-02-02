#!/usr/bin/env python3
"""
This module implements the MRUCache method
"""

from collections import OrderedDict
from typing import Any

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    This class implements the MRU caching
    """

    def __init__(self):
        """
        Initialize the MRU caching class
        """
        super().__init__()
        self.queue = OrderedDict()

    def put(self, key: Any, item: Any) -> None:
        """
        Add a new item to the MRU cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.move_to_end(key)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key, _ = self.queue.popitem(last=True)
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))

            self.queue[key] = None
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """
        Get an item from the MRU cache
        """
        if key is not None and key in self.cache_data:
            self.queue.move_to_end(key)
            return self.cache_data[key]
        return None
