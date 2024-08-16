#!/usr/bin/env python3
"""
5. Implementing an expiring web cache and tracker
"""
import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Count the number of requests to a particular URL."""

    @wraps(method)
    def wrapper(*args, **kwargs):
        key = f"count:{args[0]}"
        r.incr(key)
        r.expire(key, 10)
        return method(*args, **kwargs)

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Get the HTML content of a particular URL and return it."""
    return requests.get(url).text
