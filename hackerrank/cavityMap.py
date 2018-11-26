#!/bin/python3

import sys


def cavityMap(n, grid):
    for idx in range(1, n - 1):
        for idy in range(1, n - 1):
            up = grid[idx - 1][idy]
            right = grid[idx + 1][idy]
            left = grid[idx][idy - 1]
            down = grid[idx][idy + 1]
            if grid[idx][idy] > max(up, right, left, down):
                grid[idx] = grid[idx][0:idy] + 'X' + grid[idx][idy + 1:]
    return grid


if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    grid_i = 0
    for grid_i in range(n):
        grid_t = str(input().strip())
        grid.append(grid_t)
    result = cavityMap(n, grid)
    print("\n".join(map(str, result)))
