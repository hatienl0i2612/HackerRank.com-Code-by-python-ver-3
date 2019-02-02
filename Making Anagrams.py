#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
# def build(s):
#     map = {}
#     for char in s:
#         if char not in map:
#             map[char] = 1
#         else:
#             map[char] += 1
#     return map
# def makingAnagrams(s1, s2):
#     map1 = build(s1)
#     map2 = build(s2)
#     ans = 0
#     for key in map2.keys():
#         if key not in map1:
#             ans += map2[key]
#         else:
#             ans += max(0,map2[key] - map1[key])
#
#     for key in map1.keys():
#         if key not in map2:
#             ans += map1[key]
#         else:
#             ans += max(0,map1[key] - map2[key])
#     print(ans)

def makingAnagrams(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            s2.remove(s2[s2.index(s1[i])])
        else:
            count += 1
    print(count + len(s2))

if __name__ == '__main__':\

    s1 = list(input().strip())

    s2 = list(input().strip())
    result = makingAnagrams(s1, s2)
