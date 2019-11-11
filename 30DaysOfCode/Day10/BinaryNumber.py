#Problem available at: https://www.hackerrank.com/challenges/30-binary-numbers/problem
 #!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    count = 0
    max_1 = 0
    
    bin_rep = "{0:b}".format(n)
    for i in range(len(bin_rep)):
        if (bin_rep[i]== '1'):
            count +=1
        else:
            count = 0
        if(count>max_1):
            max_1= count
    print(max_1)
