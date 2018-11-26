#!/bin/python3

import sys

MIN_VALUE = 1


def queensAttack(n, k, r_q, c_q, obstacles):
    ' Find avaible point len for queen'
    move_count = 0
    for idx in range(-1, 2):
        for idy in range(-1, 2):
            if idx == 0 and idy == 0:
                continue
            r_q_var = r_q
            c_q_var = c_q
            while True:
                value_x = r_q_var + idx
                value_y = c_q_var + idy
                sq = [value_x, value_y]
                if obstacles.__contains__(sq):
                    break
                if value_x < MIN_VALUE or value_y < MIN_VALUE or value_x > n or value_y > n:
                    break
                move_count += 1
                r_q_var = value_x
                c_q_var = value_y
    return move_count


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]
    obstacles = []
    for obstacles_i in range(k):
        obstacles_t = [int(obstacles_temp) for obstacles_temp in input().strip().split(' ')]
        obstacles.append(obstacles_t)
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
