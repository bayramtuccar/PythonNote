#!/bin/python3

import sys

UP_INPUT_TEXT = "U"
DOWN_INPUT_TEXT = "D"

EQUEL_TEXT = "_"
UP_TEXT = "/"
DOWN_TEXT = "\\"


def inc_dec_index(cur_text, new_text):
    ' Calculate index shift'
    inc_idx = 0
    cur_char = cur_text[cur_text.__len__() - 1]
    if cur_char.__eq__(new_text):
        if new_text.__eq__(UP_TEXT):
            inc_idx += 1
        elif new_text.__eq__(DOWN_TEXT):
            inc_idx -= 1
    elif cur_char.__eq__(EQUEL_TEXT) and new_text.__eq__(DOWN_TEXT):
        inc_idx -= 1
    return inc_idx


def countingValleys(n, s):
    ' Draw the path '
    cur_idx = 0
    text_dic = {0: EQUEL_TEXT}
    for idx in range(n):
        new_text = None
        cur_char = s[idx]
        if UP_INPUT_TEXT.__eq__(cur_char):
            new_text = UP_TEXT
        elif DOWN_INPUT_TEXT.__eq__(cur_char):
            new_text = DOWN_TEXT
        inc_idx = 0
        try:
            cur_text = text_dic[cur_idx]
            inc_idx = inc_dec_index(cur_text, new_text)
            cur_idx += inc_idx
            text_dic[cur_idx] = text_dic[cur_idx] + new_text
        except:
            new_text = (idx + 1) * " " + new_text
            text_dic[cur_idx] = new_text
        for key in text_dic.keys():
            if key != cur_idx:
                text_dic[key] = text_dic[key] + " "
    text_dic[0] = text_dic[0] + "_"
    keys = text_dic.keys()
    s_keys = sorted(keys, reverse=True)
    res_text = ""
    for s_key in s_keys:
        res_text += text_dic[s_key] + "\n"
    return res_text


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
