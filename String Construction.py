#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the stringConstruction function below.

def stringConstruction(s):
    print(len(set(s)))


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)
