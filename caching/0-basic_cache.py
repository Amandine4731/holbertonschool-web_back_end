#!/usr/bin/python3
""" basic caching system """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ basic caching system """
    def put(self, key, item):
        """ put element to the dict """
        if(key != None and item != None):
            self.cache_data[key] = item

    def get(self, key):
        """ get element in the dict """
        if(key == None or key not in self.cache_data):
            return None
        return self.cache_data[key]
