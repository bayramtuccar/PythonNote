#!/bin/python3

import sys


def climbingLeaderboard(scores, alice):
    ' Find the order seq '
    s_scores = sorted(scores, reverse=True)
    cur_score = s_scores[0]
    person_count = {}
    board_count = {}
    p_count = -1
    b_count = 1
    t_count = 0
    for s_mem in s_scores:
        t_count += 1
        p_count += 1
        done = False
        if cur_score != s_mem:
            board_count[b_count] = cur_score
            person_count[cur_score] = p_count
            cur_score = s_mem
            b_count += 1
            done = True
        if t_count == s_scores.__len__():
            board_count[b_count] = cur_score
            if not done:
                p_count += 1
            person_count[cur_score] = p_count
        if done:
            p_count = 0
    result = []
    for s_alice in alice:
        alice_board = 1
        b_t_count = 0
        for keyx in board_count.keys():
            b_t_count += 1
            score = board_count[keyx]
            if score > s_alice:
                alice_board += 1
                if b_t_count == board_count.__len__():
                    result.append(alice_board)
            else:
                result.append(alice_board)
                break
    return result


def climbingLeaderboardFast(scores, alice):
    set_scores = set(scores)
    list_scores = list(set_scores)
    list_scores.sort()
    leng = len(list_scores) + 1
    lo = 0
    for score in alice:
        rank = leng
        hi = leng - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if list_scores[mid] <= score:
                lo = mid + 1
            else:
                hi = mid  #
        rank -= lo
        print(rank)


if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboardFast(scores, alice)
    # print ("\n".join(map(str, result)))
