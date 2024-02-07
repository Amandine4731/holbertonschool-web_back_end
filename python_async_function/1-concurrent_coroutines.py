#!/usr/bin/env python3
""" import the function of 0-basic_async_syntax.py,
    write an async routine that takes in 2 int arguments
    (in this order): n and max_delay.
    Spawn wait_random n times with the specified max_delay.
"""


import asyncio, random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns wait_random n times with the specified max_delay """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
