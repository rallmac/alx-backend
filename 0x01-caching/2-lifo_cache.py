#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system """

    def __init__(self):
        """ Initialize the class with the parent class's init method """
        super().__init__()
        self.last_key = None  # To track the last added key

    def put(self, key, item):
        """ Add an item in the cache with LIFO eviction policy """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.cache_data:
                self.last_key = key

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)

                self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
