#!/usr/bin/env python3
''' task 2 '''

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''multiple coroutines'''
    wait = (wait_random(max_delay) for i in range(n))
    res = await asyncio.gather(*wait)
    return (sorted(res))
