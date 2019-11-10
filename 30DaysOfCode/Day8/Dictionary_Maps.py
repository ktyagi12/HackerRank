#Problem available at: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(input())
phone_book = {}

for _ in range(n):
    element = list(map(str, input().rstrip().split()))
    phone_book[element[0]] =(element[1])
#print(phone_book)

s = input()
while(s):
    if phone_book.__contains__(s):
        print (s+"="+phone_book[s])
    else:
        print('Not found')
    s = sys.stdin.readline().strip()
