#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    ans = 0
    for i in range(len(s)//2):
        if s[-1 - i] != s[i]:
           ans += abs(ord(s[-1-i]) - ord(s[i]))
    print(ans)
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)
