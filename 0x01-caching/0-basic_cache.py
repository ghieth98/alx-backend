#!/usr/bin/env python3
"""
class BasicCache that inherits from BaseCaching and is a caching system
"""
from typing import Any

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache with no Limit
    """

    def __init__(self):
        super().__init__()

    def get(self, key: Any) -> Any:
        """
        Get item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]

    def put(self, key: Any, item: Any) -> None:
        """
        Put item by key into cache and frequency dictionary.
        """
        if key and item:
            self.cache_data[key] = item
