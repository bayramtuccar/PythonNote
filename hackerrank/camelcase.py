#!/bin/python3

import sys


def camelcase(s):
    word_count = 0 if s.__len__() == 0 else 1
    for s_char in s:
        if s_char.isupper():
            word_count += 1
    return word_count


if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
