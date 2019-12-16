#Problem available at: https://www.hackerrank.com/challenges/grading/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def next_multiple(i):
    return ((int(i/5)+1)*5)

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] <= 37:
            pass
        else:
            m = next_multiple(grades[i])
            if (m-grades[i])<3:
                grades[i] = grades[i] + (m-grades[i])
    return grades






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
