#!/usr/bin/env python3
""" import the function of 1-concurrent_coroutines.py,
    write a function that takes in 2 int arguments
    (in this order): n and max_delay
    that measures the total execution time for wait_n
    and returns total_time / n. Your function should return a float.
"""


import asyncio, time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
