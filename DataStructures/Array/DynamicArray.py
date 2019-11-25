#Problem available at: https://www.hackerrank.com/challenges/dynamic-array/problem

#!/bin/python3
import os

def dynamicArray(n, queries):
   lastAns =list()
   seqList = list()
   lastAnswer = 0
   seqList = [[] for i in range(n)]

   for query in queries:
       x = query[1]
       y = query[2]
       seq = (x ^ lastAnswer) %n
       if query[0] == 1:
            seqList[seq].append(y)
       else:
           size = len(seqList[seq])
           lastAnswer = seqList[seq][y % size]
           lastAns.append(lastAnswer)
   return lastAns

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
