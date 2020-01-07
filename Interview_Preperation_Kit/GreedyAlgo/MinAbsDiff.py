#Problem available at: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
#!/bin/python3

import math
import os
import random
import re
import sys


def minimumAbsoluteDifference(arr):
    arr.sort()
    min_abs = float('inf')
    for i in range(len(arr)-1):
        if (abs(arr[i]-arr[i+1]) < min_abs):
            min_abs = abs(arr[i] - arr[i+1])

    return min_abs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
