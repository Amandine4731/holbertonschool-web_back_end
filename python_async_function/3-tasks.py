#!/usr/bin/env python3
""" import the function of 0-basic_async_syntax.py,
    function that takes an integer max_delay and returns a asyncio.Task.
"""


import asyncio, random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    t = asyncio.create_task(wait_random(max_delay))
    return t
