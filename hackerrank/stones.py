#!/bin/python3

import sys


def stones(n, a, b):
    res_list = []
    for i in range(n):
        res = (n - 1 - i) * a + i * b
        res_list.append(res)
    return sorted(set(res_list))


if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        print(" ".join(map(str, result)))
