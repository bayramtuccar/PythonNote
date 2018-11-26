#!/bin/python3

import sys
import math


def flatlandSpaceStations(n, c):
    l = len(c)
    c.sort()
    retVal = max(c[0], n - 1 - c[l - 1])
    for i in range(1, l):
        dif = c[i] - c[i - 1] - 1
        mid = math.ceil(dif / 2)
        retVal = max(retVal, mid)
    return retVal


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = flatlandSpaceStations(n, c)
    print(result)
