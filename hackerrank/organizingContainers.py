#!/bin/python3

import sys

POSSIBLE_STR = "Possible"
IMPOSSIBLE_STR = "Impossible"


def organizingContainers(size, container):
    type_list = [0] * size
    for idx in range(size):
        list = container[idx]
        for mem in list:
            type_list[idx] += mem
    total_count = 0
    for idx in range(size):
        total_count += type_list[idx] % size
    return POSSIBLE_STR if total_count % 2 == 0 else IMPOSSIBLE_STR


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
            container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
            container.append(container_t)
        result = organizingContainers(n, container)
        print(result)
