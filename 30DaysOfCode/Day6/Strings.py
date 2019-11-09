# Problem available at: https://www.hackerrank.com/challenges/30-review-loop/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

s1 = ''
s2 = ''
num_testcases = int(input())
for i in range(num_testcases):
   in_string = input()
   for j in range(len(in_string)):
    if j%2 == 0:
        s1 = s1 + in_string[j]
    else:
        s2 = s2 + in_string[j]
   print(s1,s2)
   s1 = ''
   s2 = ''