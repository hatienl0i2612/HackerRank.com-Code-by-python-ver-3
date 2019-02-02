#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    if s[0] == s:
        sys.stdout.write('NO\n')
        return
    else:
        for i in range(1,len(s)):
            stack = []
            stack.append(s[:i])
            while len(''.join(stack)) < len(s):
                stack.append(str(int(stack[-1]) + 1))
            if ''.join(stack) == s:
                sys.stdout.write('YES ' + stack[0] + '\n')
                return
    sys.stdout.write('NO\n')
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
