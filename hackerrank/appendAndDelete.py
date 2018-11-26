#!/bin/python3

import sys

EMPTY_STR = ''
NO_STR = 'No'
YES_STR = 'Yes'


def findCommonStr(s, t):
    ' Find common text and len'
    if s.__eq__(t):
        return s, s.__len__()
    else:
        common_text = EMPTY_STR
        size = min(s.__len__(), t.__len__())
        for idx in range(size):
            if s[idx] == t[idx]:
                common_text += s[idx]
            else:
                break
        return common_text, idx


def appendAndDelete(s, t, k):
    ' Convert a str to b str with exact operation '
    c_str, idx = findCommonStr(s, t)
    retVal = NO_STR
    min_o = s.__len__() - idx + t.__len__() - idx
    r_o = k - min_o
    if r_o >= 0 and (r_o % 2 == 0 or r_o - 2 * idx > 0):
        retVal = YES_STR
    return retVal


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
