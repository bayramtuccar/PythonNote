#!/bin/python3

import sys


def serviceLane(cases, widths):
    ret_list = []
    for case in cases:
        cur_widths = widths[case[0]:case[1] + 1]
        ret_list.append(min(cur_widths))
    return ret_list


if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    width = list(map(int, input().strip().split(' ')))
    cases = []
    for cases_i in range(t):
        cases_t = [int(cases_temp) for cases_temp in input().strip().split(' ')]
        cases.append(cases_t)
    result = serviceLane(cases, width)
    print("\n".join(map(str, result)))
