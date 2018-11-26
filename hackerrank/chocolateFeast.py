#!/bin/python3

import sys


def calcExtra(t, m):
    if t < m:
        return 0
    t_new = t // m
    t_wr = t % m
    return t_new + calcExtra(t_wr + t_new, m)


def chocolateFeast(n, c, m):
    t = n // c
    return t + calcExtra(t, m)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        result = chocolateFeast(n, c, m)
        print(result)
