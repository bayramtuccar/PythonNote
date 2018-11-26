#!/bin/python3

import sys
import math


def nonDivisibleSubset(k, arr):
    mod_arr = [0] * k
    for mem in arr:
        mod_arr[mem % k] += 1
    ret_val = min(mod_arr[0], 1)
    for idx in range(1, k // 2 + 1):
        if idx != k - idx:
            ret_val += max(mod_arr[idx], mod_arr[k - idx])
    if k % 2 == 0:
        ret_val += 1
    return ret_val


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)
