#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
char = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','z','x','w','y','j','v']
def twoStrings(s1, s2):
    for i in char:
        if i in s1 and i in s2:
            print("YES")
            return
    else:
        print('NO')
        return 
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input().strip()

        s2 = input().strip()

        result = twoStrings(s1, s2)

