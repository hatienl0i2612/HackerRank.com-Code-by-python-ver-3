#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    count = 0
    for i in range(len(b)):
        # print(b[i-2:i+1])
        if b[i-2:i+1] == [0,1,0]:
            count += 1
            b[i] = 1
    print(count)


if __name__ == '__main__':

    n = int(input())

    b = [int(c) for c in input().strip()]
    try:
        result = beautifulBinaryString(b)
    except:
        pass
