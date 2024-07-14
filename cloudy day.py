#!/bin/python3
import os
import sys
from collections import defaultdict

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
    n = len(p)
    m = len(y)

    events = []
    for i in range(n):
        events.append((x[i], 'town', p[i]))

    for j in range(m):
        events.append((y[j] - r[j], 'cloud_start', j))
        events.append((y[j] + r[j] + 1, 'cloud_end', j))

    events.sort()

    cc = defaultdict(int)
    c_clouds = set()
    asp = 0
    ri = defaultdict(int)

    for event in events:
        if event[1] == 'town':
            if len(c_clouds) == 0:
                asp += event[2]
            elif len(c_clouds) == 1:
                cloud_id = next(iter(c_clouds))
                ri[cloud_id] += event[2]
        elif event[1] == 'cloud_start':
            cc[event[2]] = 0
            c_clouds.add(event[2])
        elif event[1] == 'cloud_end':
            c_clouds.remove(event[2])

    max_swr = max(ri.values(), default=0)

    return asp + max_swr

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



