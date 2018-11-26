#!/bin/python3

import sys


def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if v1 <= v2:
        return "NO"
    dif_pos = x2 - x1
    dif_vel = v1 - v2
    if dif_pos % dif_vel == 0:
        return "YES"
    return "NO"


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
