#!/bin/python3

import sys
import math


def squares(a, b):
    ' Find the root in a cer. area '
    min = int(math.ceil(math.pow(a, 0.5)))
    max = int(math.floor(math.pow(b, 0.5)))
    return max - min + 1


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)
