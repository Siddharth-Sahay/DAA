#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    dp = [0] * (k + 1)
    
    for i in range(k + 1):
        for w in arr:
            if w <= i:
                dp[i] = max(dp[i], dp[i - w] + w)
    
    return dp[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
