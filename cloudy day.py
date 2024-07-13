#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    tp = sorted(zip(x, p))
    cov = []
    for i in range(len(y)):
        cov.append((y[i] - r[i], y[i] + r[i], i))
    cov.sort()
    sp = 0
    t_covered = [0] * len(x)
    cp = [0] * len(y)
    town_map = [[] for _ in range(len(y))]
    i = 0
    for town_idx, (pos, pop) in enumerate(tp):
        while i < len(cov) and cov[i][1] < pos:
            i += 1
        for j in range(i, len(cov)):
            if cov[j][0] <= pos <= cov[j][1]:
                town_map[cov[j][2]].append(town_idx)
                cp[cov[j][2]] += pop
                t_covered[town_idx] += 1
    
    for j, (pos, pop) in enumerate(tp):
        if t_covered[j] == 0:
            sp += pop

    max_sunny_population = sp
    
    for i in range(len(y)):
        current_sunny_population = sp
        for town_idx in town_map[i]:
            if t_covered[town_idx] == 1:
                current_sunny_population += tp[town_idx][1]
        max_sunny_population = max(max_sunny_population, current_sunny_population)
    
    return max_sunny_population

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))
    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())
    y = list(map(int, input().rstrip().split()))
    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')
    fptr.close()


