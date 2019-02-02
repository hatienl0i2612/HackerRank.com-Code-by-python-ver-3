#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==m:
                print(i+1, j+1)
                break
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

