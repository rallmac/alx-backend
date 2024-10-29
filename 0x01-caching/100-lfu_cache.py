#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache defines an LFU caching system """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.usage_count = {}
        self.access_order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache with LFU eviction policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self.access_order.move_to_end(key)
        else:
            self.cache_data[key] = item
            self.usage_count[key] = 1
            self.access_order[key] = None

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                min_freq = min(self.usage_count.values())
                lfu_candidates = [
                    k for k, v in self.usage_count.items() if v == min_freq
                ]
                lfu_keys = lfu_candidates

                if len(lfu_keys) > 1:
                    lfu_key = next(iter(self.access_order))
                    while lfu_key not in lfu_keys:
                        lfu_key = next(iter(self.access_order))
                else:
                    lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.usage_count[lfu_key]
                self.access_order.pop(lfu_key)
                print("DISCARD:", lfu_key)

        self.access_order.move_to_end(key)

    def get(self, key):
        """ Get an item by key, updating its frequency and
            access order
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_count[key] += 1
        self.access_order.move_to_end(key)
        return self.cache_data[key]
