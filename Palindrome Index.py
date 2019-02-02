#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the palindromeIndex function below.
def isPalindrome(s):
    for idx in range(len(s) // 2):
        if s[idx] != s[len(s) - idx - 1]:
            return False
    return True


def palindromeIndex(s):
    for i in range((len(s) + 1) // 2):
        if s[i] != s[len(s) - i - 1]:
            if isPalindrome(s[:i] + s[i + 1:]):
                print(i)
                return
            else:
                print(len(s) - i - 1)
                return
    print('-1')
    return


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
