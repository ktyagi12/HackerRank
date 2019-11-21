#Problem available at: https://www.hackerrank.com/challenges/30-regex-patterns/problem
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    l = []
    for N_itr in range(N):
       
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if (emailID[-10:]) == '@gmail.com':
            l.append(firstName)

        #print(l)
    l.sort()
    for i in l:
        print(i)
