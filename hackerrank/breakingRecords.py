#!/bin/python3

import sys

REC_HIGH_INDEX = 0
REC_LOW_INDEX = 1


def breakingRecords(score):
    result = [0, 0]
    if score.__len__() <= 1:
        return result
    min_s = score[0]
    max_s = score[0]
    for s in score:
        if min_s > s:
            min_s = s
            result[REC_LOW_INDEX] += 1
        if max_s < s:
            max_s = s
            result[REC_HIGH_INDEX] += 1
    return result


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print(" ".join(map(str, result)))
