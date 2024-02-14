#!/usr/bin/python3
""" BasicCaching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Caching system with fifo algorythm """

    def __init__(self):
        """
        init
        """
        super().__init__()

    def put(self, key, item):
        """ add element to dict of cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                del self.cache_data[first_item]
                print(f"DISCARD: {first_item}")
            self.cache_data[key] = item

    def get(self, key):
        """ get element of dict by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
