#!/bin/python3

import sys

NUMBER_LIST = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
               'fifteen', 'sixteen', 'seventeen', 'eighteen', 'ninteen', 'twenty']

WORD_LIST = ["%s o' clock", "quarter past %s", "half past %s", "quarter to %s"]


def timeInWords(h, m):
    for i in range(1, 10):
        NUMBER_LIST.append('twenty %s' % NUMBER_LIST[i])
    hour = NUMBER_LIST[h] if (m < 31) else NUMBER_LIST[h + 1]
    if not m % 15:
        ret_val = WORD_LIST[m // 15] % hour
    elif m < 30:
        ret_val = "%s minute" % NUMBER_LIST[m] + "s" * (0 if m == 1 else 1) + " past %s" % hour
    else:
        ret_val = "%s minute" % NUMBER_LIST[60 - m] + "s" * (0 if m == 59 else 1) + " to %s" % hour
    return ret_val


if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
