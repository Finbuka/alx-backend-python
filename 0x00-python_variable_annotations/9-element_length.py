#!/usr/bin/env python3
'''task 9'''
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return a sequence '''

    return [(i, len(i)) for i in lst]
