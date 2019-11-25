#Problem available at: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks_dict = dict()
    pairs = 0
    for i in ar:
        if socks_dict.__contains__(i):
            socks_dict[i] = socks_dict[i] +1
        else:
            socks_dict[i] = 1
    #print('dict:', socks_dict)
    for j in socks_dict.keys():
        if socks_dict[j] >1:
            pairs = pairs+ int(socks_dict[j]/2)
    #print('Pairs: ',pairs)
    return pairs



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
