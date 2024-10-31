#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system """

    def __init__(self):
        """ Initialize the class with the parent class's
            init method
        """
        super().__init__()
        self.cache_data = OrderedDict()  # To track the last added key

    def put(self, key, item):
        """ Add an item in the cache with LIFO eviction policy """
        if key is None or item is None:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_item, _ = self.cache_data.popitem(Tru)
                print("DISCARD:", last_item)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ The get method """
        return self.cache_data.get(key, None)
