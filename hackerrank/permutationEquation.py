#!/bin/python3

import sys


def permutationEquation(p):
    ' Find the y value '
    dic = {}
    for idx, p_mem in enumerate(p):
        dic[p_mem] = idx + 1
    result = []
    for idy in range(1, p.__len__() + 1):
        result.append(dic[dic[idy]])
    return result


if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p)
    print("\n".join(map(str, result)))
