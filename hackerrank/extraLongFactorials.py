#!/bin/python3

import sys

factorial = lambda x: x * factorial(x - 1) if x > 1 else 1


def extraLongFactorials(n):
    print(factorial(n))


if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
