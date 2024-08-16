#!/usr/bin/env python3
"""
5. Implementing an expiring web cache and tracker
"""

# In this tasks, we will implement a get_page function (prototype: def get_page(url: str) -> str:). The core of the function is very simple. It uses the requests module to obtain the HTML content of a particular URL and returns it.

# Start in a new file named web.py and do not reuse the code written in exercise.py.

# Inside get_page track how many times a particular URL was accessed in the key "count:{url}" and cache the result with an expiration time of 10 seconds.

# Tip: Use http://slowwly.robertomurray.co.uk to simulate a slow response and test your caching.

# Bonus: implement this use case with decorators.

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def count_access(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(url: str) -> str:
        r.incr(f"count:{url}")
        return func(url)

    return wrapper


@count_access
def get_page(url: str) -> str:
    key = f"cached:{url}"
    content = r.get(key)
    if content is None:
        content = requests.get(url).text
        r.setex(key, 10, content)
    return content
