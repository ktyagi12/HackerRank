#Problem available at: https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    flag = False
    s1_dict=dict()
    s2_dict=dict()
    for i in s1:
        if(s1_dict.__contains__(i)):
            s1_dict[i] =s1_dict[i] +1
        else:
            s1_dict[i] =1
    print(s1_dict)
    for j in s2:
        if(s2_dict.__contains__(j)):
            s2_dict[j] =s2_dict[j] +1
        else:
            s2_dict[j] =1
    print(s2_dict)
    for _ in s1:
        if (s2_dict.__contains__(_)):
            flag = True
            break
        else:
            flag = False
    if(flag):
        return ('YES')
    else:
        return('NO')
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
