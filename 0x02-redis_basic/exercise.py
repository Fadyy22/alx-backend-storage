#!/usr/bin/env python3
"""module for redis tasks in python"""

from typing import Union
from uuid import uuid4
import redis


class Cache:
    """class Cache for using redis client cache"""

    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data passed in redis client and return the key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
