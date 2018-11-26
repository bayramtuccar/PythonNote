#!/bin/python3

import sys


def cutTheSticks(arr):
    ' Find the cutted stick number '
    ret_list = []
    while True:
        arr_len = arr.__len__()
        if arr_len == 0:
            break
        ret_list.append(arr_len)
        min_mem = min(arr)
        for idx in range(arr_len).__reversed__():
            new_value = arr[idx] - min_mem
            if new_value > 0:
                arr[idx] = new_value
            else:
                del arr[idx]
    return ret_list


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = cutTheSticks(arr)
    print("\n".join(map(str, result)))
