#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def check(s):
    if 'AA' in s or 'BB' in s:
        return True
    return False
def alternatingCharacters(s):
    if not 'A' in s or not 'B' in s:
        print(len(s) - 1)
        return
    else:
        a = 0
        b = 0
        qua = False
        if check(s):
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    qua += 1
            print(qua)
        else:
            print('0')
            return
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
