#!/bin/python3

import sys


def pickingNumbers(a):
    res_dic = {}
    len = max(a) + 1
    for idx in range(len):
        res_dic[idx] = a.count(idx)

    prev_key = -2
    prev_value = 0
    result = -1
    for key in res_dic.keys():
        value = res_dic[key]
        if prev_key + 1 == key:
            result = max(result, prev_value + value)
        prev_key = key
        prev_value = value
    return result


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)
