#!/usr/bin/env python3
''' task 10'''
from typing import Any, Sequence, Union

# The types of the elements of the input are not know


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' to retrieve the 1st element of the sequence if exists '''
    if lst:
        return lst[0]
    else:
        return None
