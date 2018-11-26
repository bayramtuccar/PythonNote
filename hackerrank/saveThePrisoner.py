#!/bin/python3

import sys


def findThePrisoner(t, n):
    return n if n == t else n % t


def saveThePrisoner(total, sweet, cur):
    ' Find the last member '
    move = sweet % total - 1
    move = move % total
    return findThePrisoner(total, cur + move)


t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
