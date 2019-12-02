#Problem available at: https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    flag = False
    magazine_dict = dict()
    for mag in magazine:
        if(magazine_dict.__contains__(mag)):
            magazine_dict[mag] = magazine_dict[mag]+1
        else:
            magazine_dict[mag] = 1

    for n in note:
        if(magazine_dict.__contains__(n) and magazine_dict[n]!=0):
            magazine_dict[n] = magazine_dict[n]-1
            flag = True
        else:
            flag = False
            break
    if(flag):
        print('Yes')        
    else:
        print('No')        


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
