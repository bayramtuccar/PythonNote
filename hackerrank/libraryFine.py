#!/bin/python3

import sys
from datetime import date


def libraryFine(d1, m1, y1, d2, m2, y2):
    ' Find the lib. fee '
    d_r = date(y1, m1, d1)
    d_e = date(y2, m2, d2)
    fee = 0
    if d_r > d_e:
        if d_r.year == d_e.year:
            if d_r.month == d_e.month:
                fee = 15 * (d_r.day - d_e.day)
            else:
                fee = 500 * (d_r.month - d_e.month)
        else:
            fee = 10000
    return fee


if __name__ == "__main__":
    d1, m1, y1 = input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
