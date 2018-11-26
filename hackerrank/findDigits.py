#!/bin/python3

import sys


def getDigits(n):
    list = []
    total_num = n
    if total_num < 10:
        list.append(total_num)
    else:
        while True:
            cur_digit = total_num % 10
            list.append(int(cur_digit))
            total_num = round(total_num / 10, 0)
            if total_num < 1:
                break
    return list


def findDigits(n):
    n_digit_list = getDigits(n)
    result_count = 0
    for n_digit in n_digit_list:
        if n_digit > 0 and (n / n_digit) % 2 == 0:
            result_count += 1
    return result_count


def findDigitsAsStr(n):
    n_digit_list = str(n)
    result_count = 0
    for n_str in n_digit_list:
        n_digit = int(n_str)
        if n_digit > 0 and (n / n_digit) % 2 == 0:
            result_count += 1
    return result_count


def findDigitsLine(n):
    return sum(int(x) != 0 and n % int(x) == 0 for x in str(n))


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigitsLine(n)
        print(result)
