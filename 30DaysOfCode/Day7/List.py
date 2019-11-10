#Problem available at: https://www.hackerrank.com/challenges/30-arrays/problem
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n in range(1,1001):
        arr = list(map(int, input().rstrip().split()))
        
    for i in range(1, len(arr)+1):
        print (arr[-i], end=' ')
