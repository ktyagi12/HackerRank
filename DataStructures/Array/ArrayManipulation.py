#Problem available at: https://www.hackerrank.com/challenges/crush/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr =[0] * (n+2)
    sum_ele = 0
    max_ele = 0
    for q in queries:
        x = q[0]
        y = q[1]
        ele = q[2]
        arr[x] = arr[x]+ele
        arr[y+1] = arr[y+1] - ele

    for i in range(0,len(arr)):
        sum_ele = sum_ele + arr[i]
        if(sum_ele>max_ele):
            max_ele = sum_ele
    return(max_ele)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
