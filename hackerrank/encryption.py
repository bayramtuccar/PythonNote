#!/bin/python3

import sys
import math


def encryption(s):
    s_local = s.replace(' ', '')
    l = math.ceil(math.pow(len(s_local), 0.5))
    list = []
    for idx in range(l):
        size = min(l, len(s_local))
        list.append(s_local[0:size])
        s_local = s_local[size:]
    ret = ''
    for idx in range(l):
        add = False
        for idy in range(l):
            if len(list[idy]) < idx + 1:
                break
            ret += list[idy][idx]
            add = True
        if add:
            ret += ' '
    return ret


if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
