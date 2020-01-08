#Problem available at: https://www.hackerrank.com/challenges/equal-stacks/problem

#!/bin/python3

import os
import sys

def equalStacks(h1, h2, h3):
    stack1 = []
    stack2 = []
    stack3 = []
    
    height_stack1 = height_stack2 = height_stack3 = 0
    min_height_stack = 0

    for i in range(len(h1)-1,-1,-1):
        stack1.append(h1[i])
        height_stack1 = height_stack1 + h1[i]

    for i in range(len(h2)-1,-1,-1):
        stack2.append(h2[i])
        height_stack2 = height_stack2 + h2[i]

    for i in range(len(h3)-1,-1,-1):
        stack3.append(h3[i])
        height_stack3 = height_stack3 + h3[i]
    
    min_height_stack = min(height_stack1, min(height_stack2, height_stack3))

    while(height_stack1!= height_stack2 or height_stack2!= height_stack3):

        while (height_stack1 > min_height_stack):
            height_stack1 = height_stack1 - stack1.pop()
        
        min_height_stack = min(height_stack1, min(height_stack2, height_stack3))

        while (height_stack2 > min_height_stack):
            height_stack2 = height_stack2 - stack2.pop()
        
        min_height_stack = min(height_stack1, min(height_stack2, height_stack3))

        while (height_stack3 > min_height_stack):
            height_stack3 = height_stack3 - stack3.pop()
        
        min_height_stack = min(height_stack1, min(height_stack2, height_stack3))

    return min_height_stack


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()