#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    nums=list(price)
    nums.sort()
    lsr=list()
    mincost=10**10
    for i in range(1,len(price)):
        if nums[i]-nums[i-1] < mincost and price.index(nums[i]) < price.index(nums[i-1]):
            mincost=nums[i]-nums[i-1]
    print(mincost)
if __name__ == '__main__':
    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

