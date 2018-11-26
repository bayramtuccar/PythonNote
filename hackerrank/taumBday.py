#!/bin/python3

import sys


def taumBday(b, w, x, y, z):
    return b * min(x, y + z) + w * min(x + z, y)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        b, w = input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = taumBday(b, w, x, y, z)
        print(result)
