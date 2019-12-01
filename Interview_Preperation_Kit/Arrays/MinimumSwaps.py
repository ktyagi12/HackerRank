#Problem available at: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] =temp

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    pos_arr = [0]*n

    for i in range(n):
        arr[i]=arr[i]-1
        pos_arr[arr[i]] = i

    swaps = 0
    for i in range(n):
        if(arr[i]==i):
            pass
        else:
            swaps=swaps+1
            swap(arr,i,pos_arr[i])
            swap(pos_arr,arr[i],arr[pos_arr[i]])

    return(swaps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
