#!/usr/bin/env python3
"""module for redis tasks in python"""

from functools import wraps
from typing import Callable, Union
from uuid import uuid4
import redis


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""

    @wraps(method)
    def invoker(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args)

    return invoker


def call_history(method: Callable) -> Callable:
    """
    decorator to store the history of inputs and outputs
    for a particular function
    """

    @wraps(method)
    def invoker(self, *args):
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        value = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", value)
        return value

    return invoker


class Cache:
    """class Cache for using redis client cache"""

    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
