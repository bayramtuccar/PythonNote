#!/bin/python3

import sys


def minimumDistances(a):
    a_len = a.__len__()
    min_dist = a_len
    found = False
    dic = {}
    for idx in range(a_len):
        a_char = a[idx]
        dist = None
        try:
            dist = idx - dic[a_char]
            del dic[a_char]
        except:
            dic[a_char] = idx
        if dist:
            min_dist = min(min_dist, dist)
            found = True
    return min_dist if found else -1


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)
