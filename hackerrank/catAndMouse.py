#!/bin/python3

import sys


def catAndMouse(x, y, z):
    ' Case for Cats and Mouse '
    x_diff = abs(x - z)
    y_diff = abs(y - z)
    if x_diff == y_diff:
        return "Mouse C"
    elif x_diff < y_diff:
        return "Cat A"
    elif x_diff > y_diff:
        return "Cat B"


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print("".join(map(str, result)))
