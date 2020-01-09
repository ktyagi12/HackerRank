#Problem available at: https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    val_dict = {'{': '}','(': ')','[':']','}':'{',']':'[',')':'('}
    val_list = []
    for i in range(len(s)):
        if(len(val_list) == 0):
            val_list.append(s[i])
            #print('Initial push: ', val_list)
        else:
            if (val_dict[s[i]] == val_list[-1]):
                val_list.pop(-1)
                #print('After pop: ', val_list)
            elif (s[i] == ')' or s[i] == '}' or s[i] == ']'):
                return 'NO'
            else:
                val_list.append(s[i])
                #print('Inter push: ', val_list)
                
    if (len(val_list) == 0):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
