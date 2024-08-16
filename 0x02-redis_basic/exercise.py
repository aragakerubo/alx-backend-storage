#!/usr/bin/env python3
"""
1. Reading from Redis and recovering original type
"""


import redis
import uuid
from typing import Union, Callable


# 0. Writing strings to Redis
class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    # 1. Reading from Redis and recovering original type
    def get(
        self, key: str, fn: Callable = None
    ) -> Union[str, bytes, int, float]:
        """Get data from Redis"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Get a string from Redis"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Get an integer from Redis"""
        return self.get(key, fn=lambda d: int(d))
