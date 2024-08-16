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
        cached_response = r.get(f"cached:{args[0]}")
        if cached_response:
            return cached_response.decode("utf-8")
        response = method(args[0])
        r.setex(f"cached:{args[0]}", 10, response)
        return response

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Get the HTML content of a particular URL and return it."""
    return requests.get(url).text
