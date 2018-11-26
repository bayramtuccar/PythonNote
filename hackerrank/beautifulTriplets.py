#!/bin/python3

import sys


def beautifulTriplets(d, arr):
    ret_val = 0
    for mem in arr:
        ret_val += 1 if arr.__contains__(mem + d) and arr.__contains__(mem + 2 * d) else 0
    return ret_val


if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr)
    print(result)
