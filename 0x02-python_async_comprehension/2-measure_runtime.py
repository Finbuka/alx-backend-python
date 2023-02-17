#!/usr/bin/env python3
'''task 2'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' function to measure the runtime of async_comprehension '''
    start = time.perf_counter()
    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    end = time.perf_counter()
    return end - start
