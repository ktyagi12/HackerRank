#Problem available at: https://www.hackerrank.com/challenges/sparse-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    result=list()
    string_dict = dict()
    for st in strings:
        if string_dict.__contains__(st):
            string_dict[st] = string_dict[st] +1
        else:
            string_dict[st] = 1
    for q in queries:
        if string_dict.__contains__(q):
            result.append(string_dict[q])
        else:
            result.append(0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
