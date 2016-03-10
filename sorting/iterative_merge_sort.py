#!/bin/env python
'''
'''

import math

def merge_sort(array):
    """This method will take a list/array as input, and perform a recursive
merge sort using python generators to yield the answer 1 element at a time.
This is commonly refered to as "lazy" sort.
"""

    def _threesort(a, b, c):
        if (a < b):
            if (c > b):
                yield a; yield b; yield c
            elif (c > a):
                yield a; yield c; yield b
            else:
                yield c; yield a; yield b
        else:
            if (c > a):
                yield b; yield a; yield c
            elif (c > b):
                yield b; yield c; yield a
            else:
                yield c; yield b; yield a

    def _itr_merge_sort(start, stop):
        middle = int(start + math.floor((stop - start) / 2))
        if abs(stop - start) <= 1: 
            if array[start] < array[stop]:
                yield array[start]
                yield array[stop]
            else:
                yield array[stop]
                yield array[start]
            return
        elif abs(stop - start) <= 2:
            for i in sorted([array[start], array[middle], array[stop]]): 
                yield i
            return

        itr_left = _itr_merge_sort(start, middle)
        itr_right = _itr_merge_sort(middle+1, stop)

        left_val, right_val = None, None
        while True:
            if left_val == None:
                try: left_val = itr_left.next()
                except StopIteration: pass

            if right_val == None:
                try: right_val = itr_right.next()
                except StopIteration: pass

            if left_val != None and right_val != None:
                if left_val < right_val: 
                    yield left_val
                    left_val = None
                else: 
                    yield right_val
                    right_val = None
            elif left_val != None and right_val == None:
                yield left_val
                for i in itr_left: yield i
                return
            elif left_val == None and right_val != None:
                yield right_val
                for i in itr_right: yield i
                return
            else:
                return

    return _itr_merge_sort(0, len(array) - 1)

if __name__ == "__main__":
    import sys

    a = []
    for l in sys.stdin:
        a.append(int(l.strip()))

    for i in merge_sort(a):
        print i

