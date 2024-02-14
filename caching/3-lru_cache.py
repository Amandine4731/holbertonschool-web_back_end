#!/usr/bin/python3
""" LiFoCaching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Caching system with fifo algorythm """

    def __init__(self):
        """ Init """
        super().__init__()
        self.list_keys = []

    def put(self, key, item):
        """ Add element to cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.list_keys.remove(key)
                else:
                    least_recently_key = self.list_keys.pop(0)
                    del self.cache_data[least_recently_key]
                    print(f"DISCARD: {least_recently_key}")
            self.list_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get element from cache """
        if key is None or key not in self.cache_data:
            return None
        self.list_keys.remove(key)
        self.list_keys.append(key)
        return self.cache_data[key]
