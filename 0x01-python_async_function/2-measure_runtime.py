#!/usr/bin/env python3
'''task 2'''

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' function to measure the runtime'''
    st = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - st
    return total_time / n
