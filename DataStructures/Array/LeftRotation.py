#Problem available at: https://www.hackerrank.com/challenges/array-left-rotation/problem

#!/bin/python3

import math
import os
import random
import re
import sys



def left_rotate(a,n,d):
    for i in range(d):
        temp = a.pop(0)
        a.append(temp)
    print(' '.join(map(str,a)))
        
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    left_rotate(a,n,d)
