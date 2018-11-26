#!/bin/python3

import sys

NO_STR = "NO"
YES_STR = "YES"
SEARCH_STR = "hackerrank"


def hackerrankInString(s):
    ret_val = NO_STR
    searched_idx = 0
    cur_idx = 0
    while True:
        cur_idx = s.index(SEARCH_STR[searched_idx], cur_idx)
        if cur_idx < 0:
            break
        searched_idx += 1
        if searched_idx == SEARCH_STR.__len__():
            ret_val = YES_STR
            break
    return ret_val


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
