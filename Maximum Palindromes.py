#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#
from collections import Counter


def answerQuery(s, l, r):
    # Return the answer for this query modulo 1000000007.
    x = s[l - 1:r]
    c = dict(Counter(x))
    m = {}
    n = {}
    for key, val in c.items():
        m[key] = val // 2
        n[key] = val % 2
    m = list(m.values())
    n = list(n.values())
    m = [i for i in m if i != 0]
    c1 = n.count(1)
    sum1 = math.factorial(sum(m))
    prod = 1
    for i in m:
        prod = prod * math.factorial(i)
    if (c1 == 0):
        res = sum1 // prod
    else:
        res = sum1 // prod * c1
    print(res % (pow(10, 9) + 7))
    return


if __name__ == '__main__':
    s = list(input())

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(s, l, r)
