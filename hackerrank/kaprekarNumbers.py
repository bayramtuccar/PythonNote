#!/bin/python3

import sys

INVALID_RANGE = "INVALID RANGE"


def parseStr(str):
    l = len(str)
    if l % 2 == 0:
        left = int(str[:int(l / 2)])
        right = int(str[int(l / 2):])
    else:
        str = '0' + str
        left = int(str[:int((l + 1) / 2)])
        right = int(str[int((l + 1) / 2):])
    return left, right


def kaprekarNumbers(p, q):
    ret_list = []
    for i in range(p, q):
        left, right = parseStr(str(i * i))
        if left + right == i:
            ret_list.append(i)
    if len(ret_list) == 0:
        ret_list.append(INVALID_RANGE)
    return ret_list


if __name__ == "__main__":
    p = int(input().strip())
    q = int(input().strip())
    result = kaprekarNumbers(p, q)
    print(" ".join(map(str, result)))
