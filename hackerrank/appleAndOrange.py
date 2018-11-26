#!/bin/python3

import sys


def appleAndOrange(s, t, a, b, apple, orange):
    result = []
    count = 0
    for ap in apple:
        rap = ap + a
        if (s <= rap and t >= rap):
            count += 1
    result[0] = count
    count = 0
    for o in orange:
        ro = o + b
        if (s <= ro and t >= ro):
            count += 1
    result[0] = count


if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print("\n".join(map(str, result)))
