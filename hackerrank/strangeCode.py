#!/bin/python3

import sys
import math


def strangeCode(t):
    cur_len = 3
    while t > cur_len:
        t -= cur_len
        cur_len *= 2
    return cur_len - t + 1


if __name__ == "__main__":
    t = int(input().strip())
    result = strangeCode(t)
    print(result)
