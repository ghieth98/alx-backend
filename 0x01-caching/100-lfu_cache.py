#!/usr/bin/env python3
"""
This module implements the LFUCache method
"""

from collections import OrderedDict, defaultdict
from typing import Any

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    This class implements the LFU caching
    """

    def __init__(self):
        """
        Initialize the LFU caching class
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.queue = OrderedDict()

    def put(self, key: Any, item: Any) -> None:
        """
        Add a new item to the LFU cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.queue.move_to_end(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_freq = min(self.frequency.values())
                    min_keys = [
                        k for k, v in self.frequency.items() if v == min_freq
                    ]
                    discard_key = min_keys[0]

                    if len(min_keys) == 1:
                        del self.cache_data[discard_key]
                        del self.frequency[discard_key]
                    else:
                        for k in self.queue:
                            if k in min_keys:
                                del self.cache_data[k]
                                del self.frequency[k]
                                break

                    print("DISCARD: {}".format(discard_key))

                self.cache_data[key] = item
                self.frequency[key] = 1
                self.queue[key] = None

    def get(self, key: Any) -> Any:
        """ Get an item by key.
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.queue.move_to_end(key)
            return self.cache_data[key]

        return None
