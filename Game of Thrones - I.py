#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def build(s):
    map = {}
    for char in s:
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1
    return map
def gameOfThrones(s):
    s_map = build(s)

    have = False
    for key,value in s_map.items():
        if value % 2 == 1:
            if have:
                print('NO')
                break
            have = True
    else:
        print('YES')
if __name__ == '__main__':
    s = input()

    result = gameOfThrones(s)
