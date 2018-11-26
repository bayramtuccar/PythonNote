#!/bin/python3

import sys

EMPTY_STR = "Empty String"


def super_reduced_string(s):
    while True:
        s_len = s.__len__()
        s_char_prev = None
        cont = False
        for idx in range(s_len):
            s_char = s[idx]
            if s_char_prev == s_char:
                s = s[:idx - 1] + s[idx + 1:]
                cont = True
                break
            s_char_prev = s_char
        if not cont:
            break
    return EMPTY_STR if s.__len__() == 0 else s


s = input().strip()
result = super_reduced_string(s)
print(result)
