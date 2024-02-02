#!/usr/bin/env python3
"""
class BasicCache that inherits from BaseCaching and is a caching system
"""
from typing import Any

BaseCaching = __import__("base_caching").BaceCaching


class BasicCache(BaseCaching):
    """
    BasicCache that inherits from BaseCaching
    """

    def __init__(self):
        super().__init__()

    def get(self, key: Any) -> Any:
        """
        Get a value from the cache by key
        """
        if key in self.cache_data:
            return self.cache_data[key]

    def put(self, key: Any, item: Any) -> None:
        """
        Put a value
        """
        if key and item:
            self.cache_data[key] = item
