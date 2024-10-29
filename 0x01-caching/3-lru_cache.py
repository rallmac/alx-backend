#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache defines an LRU caching system """

    def __init__(self):
        """ Initialize the class with the parent class's
            init method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache with LRU eviction policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", oldest_key)

    def get(self, key):
        """ Get an item by key, updating it as most recently
            used
        """
        if key in self.cache_data:
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        return None
