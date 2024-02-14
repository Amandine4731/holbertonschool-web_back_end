#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ return runtine execution """
    tp1 = time.time()
    result = [async_comprehension() for loop in range(4)]
    await asyncio.gather(*result)
    return (time.time() - tp1)
