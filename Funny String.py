#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the funnyString function below.
def funnyString(s):
    for i in range(1, len(s) // 2 + 1):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[len(s) - i - 1]) - ord(s[len(s) - i])):
            print('Not Funny')
            break
    else:
        print('Funny')


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)
