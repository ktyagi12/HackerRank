#Problem available at: https://www.hackerrank.com/challenges/30-bitwise-and/problem
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        xmax=0
        for i in range(n, 1, -1):
            for j in range(n, i, -1):
                temp = i&j
                if temp > xmax and temp < k:
                    xmax = temp
                
                if xmax == k-1: break
      
        print(xmax)
