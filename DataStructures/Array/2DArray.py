
#Problem available at: https://www.hackerrank.com/challenges/2d-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_list=list()
    #max_hour_glass = 0
    for i in range(0,len(arr)-2):
        for j in range(0,len(arr)-2):
            #hour_glass =0
            hour_glass= arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1] + arr[i+2][j+2]
            sum_list.append(hour_glass)
            '''
            if hour_glass>max_hour_glass:
                max_hour_glass=hour_glass
            #hour_glass = 0
            '''
    return max(sum_list)
    #return max_hour_glass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
