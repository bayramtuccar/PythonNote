#!/bin/python3

import sys


def workbook(n, k, arr):
    ret_val = 0
    p_count = 1
    for idx in range(n):
        q_count = arr[idx]
        value = q_count // k
        c_p_count = value if q_count % k == 0 else value + 1
        for idy in range(1, c_p_count + 1):
            mn = k * (idy - 1) + 1
            offset = min(k, q_count - mn + 1)
            mx = mn + offset
            if mn <= p_count and mx > p_count:
                ret_val += 1
            p_count += 1
    return ret_val


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = workbook(n, k, arr)
    print(result)
