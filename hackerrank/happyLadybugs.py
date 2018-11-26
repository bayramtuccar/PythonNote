#!/bin/python3

import sys
import re

NO_STR = "NO"
YES_STR = "YES"


def happyLadybugs(n, b):
    retVal = True
    if b.count("_") == 0 and len(re.sub(r'((.)\2+)', "", b)) != 0:
        retVal = False
    if retVal:
        for b_mem in set(b):
            if b_mem != "_" and b.count(b_mem) == 1:
                retVal = False
    return YES_STR if retVal else NO_STR


Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    result = happyLadybugs(n, b)
    print(result)
