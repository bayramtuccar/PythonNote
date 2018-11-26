#!/bin/python3

import sys


def getTotalX(a, b):
    # Complete this function
    result = []
    s_a = sorted(a)
    s_b = sorted(b)
    a_max = s_a[s_a.__len__() - 1]
    b_min = s_b[0]
    if a_max < b_min:
        for i in range(a_max, b_min + 1):
            found = True
            for a_mem in s_a:
                for b_mem in s_b:
                    if i % a_mem != 0 or b_mem % i != 0:
                        found = False
                        break
                if not found:
                    break
            if found:
                result.append(i)
    return result.__len__()


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
