#Problem available at: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

import math
def prime_or_not(n):
    if n>1:
        for i in range(2,int(math.sqrt(n))+1):
            if (n%i)==0:
                return False
        return True       
    else:
        return

T = int(input())
for i in range(T):
    num = int(input())
    check= prime_or_not(num)
    if check == True:
        print('Prime')
    else:
        print('Not prime')