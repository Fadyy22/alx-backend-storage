#!/usr/bin/env python3
"""module for redis tasks in python"""

from typing import Callable, Union
from uuid import uuid4
import redis


class Cache:
    """class Cache for using redis client cache"""

    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data passed in redis data storage and return the key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """returns a value from redis data storage by using key"""
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """returns str value for redis data storage"""
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """returns str value for redis data storage"""
        return self.get(key, fn=int)
