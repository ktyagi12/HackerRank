#Problem available at: https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    strs = list(s)
    i = 0
    j = 1
    count = 0
    while(j< len(strs)):
        if strs[i] == strs[j]:
            strs.pop(j)
            count = count +1
            
        else:
            i = i+1
            j = j+1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
