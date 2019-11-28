#Problem available at: https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    length = len(s)
    i= 0
    while(i<length):
        if s[i] == 'a':
            count=count+1
        i=i+1
    #print('Initially,count:',count)
    q=int(n/length)
    count = count*q
    #print('Now,count:',count)
    r = n%length
    for i in range(r):
        if(s[i]=='a'):
            count = count+1
    #print('Final count: ', count)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()