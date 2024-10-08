#!/usr/bin/env python3
"""
5. Implementing an expiring web cache and tracker
"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def count_access(func: Callable) -> Callable:
    """Decorator to count how many times a particular URL was
    accessed and cache the result with an expiration time of 10 seconds"""

    @wraps(func)
    def wrapper(url: str) -> str:
        """Wrapper function"""
        r.incr(f"count:{url}")
        cached_response = r.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode("utf-8")
        response = func(url)
        r.setex(f"cached:{url}", 10, response)
        return response

    return wrapper


@count_access
def get_page(url: str) -> str:
    """Get the HTML content of a particular URL"""
    return requests.get(url).text
