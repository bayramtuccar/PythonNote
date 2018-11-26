#!/bin/python3

import sys


def getMoneySpent(keyboards, drives, s):
    ' Find max spendable money '
    s_k_list = sorted(keyboards, reverse=True)
    for idx, s_k in enumerate(s_k_list):
        if s_k >= s or s_k <= 0:
            del s_k_list[idx]
    s_d_list = sorted(drives, reverse=True)
    for idx, s_d in enumerate(s_d_list):
        if s_d >= s or s_d <= 0:
            del s_d_list[idx]
    s_max = -1
    for s_k in s_k_list:
        for s_d in s_d_list:
            value = s_k + s_d
            if value == s:
                return s
            if value < s:
                s_max = max(s_max, value)
    return s_max


s, n, m = input().strip().split(' ')
s, n, m = [int(s), int(n), int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
