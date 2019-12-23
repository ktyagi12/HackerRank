#Problem available at: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for i in range(0,len(a)):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                count = count+1
                
    print('Array is sorted in %d swaps.' %count)
    print('First Element:', a[0])
    print('Last Element:',a[-1])        
            

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)