#Problem available at: https://www.hackerrank.com/challenges/30-2d-arrays/problem


#!/bin/python3

import math
import os
import random
import re
import sys

def calc_sum(arr):
    sum_list= list()
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] 
            #print('s=', s)
            sum_list.append(s)
    print(max(sum_list))
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    calc_sum(arr)
