#!/bin/python3

import sys


def fairRations(b):
    retVal = 0
    tempVal = 0
    for b_mem in b:
        tempVal = (tempVal + b_mem) % 2
        retVal += tempVal * 2
    return "NO" if tempVal else retVal


if __name__ == "__main__":
    N = int(input().strip())
    B = list(map(int, input().strip().split(' ')))
    result = fairRations(B)
    print(result)
