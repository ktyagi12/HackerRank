#Problem available at:https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(array):
    current = 0
    jumps = 0
    while(current < len(array) - 1):
        if(current <= len(array)-3):
            current = current + 2
            #print('curr+2')
        else:
            current = current + 1
            #print('curr+1')
        if c[current]==1 :
            current = current-1
            #print('current:',current)
        jumps = jumps+1
        #print('Jumps:',jumps)
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
