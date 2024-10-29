#!/usr/bin/env python3
"""This function creates a BasicCache class that inherits
   from BaseCaching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a caching system without a limit """

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key """
        return self.cache_data.get(key, None)
