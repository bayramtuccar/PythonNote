#!/bin/python3

import sys

TOTAl_ENERGY = 100

calc_energy = lambda i: 3 if i else 1


def jumpingOnClouds(c, n, k):
    ' calc energy '
    energy = TOTAl_ENERGY
    for idx in range(0, n, k):
        energy -= calc_energy(c[idx])
    return energy


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, n, k)
    print(result)
