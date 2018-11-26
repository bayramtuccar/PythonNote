#!/bin/python3

import sys


def circularArrayRotation(a, m, k):
    ' rotate the array '
    last_index_a = a.__len__() - 1
    for idx in range(k):
        last_mem = a[last_index_a]
        del a[last_index_a]
        a.insert(0, last_mem)
    result = []
    for m_mem in m:
        result.append(a[m_mem])
    return result


if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
        m_t = int(input().strip())
        m.append(m_t)
    result = circularArrayRotation(a, m, k)
    print("\n".join(map(str, result)))
