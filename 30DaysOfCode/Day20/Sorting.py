#Problem available at: https://www.hackerrank.com/challenges/30-sorting/problem
#!/bin/python3

import sys
def swap(num1,num2):
    temp = num1
    num1=num2
    num2=temp

    return num1,num2

def sort_array(a,n):
    swap_count=0
    for i in range(n):
        #print('i = ', i)
        for j in range(0,n-1-i):
            #print('j=', j)
            if a[j]> a[j+1]:
                a[j], a[j+1] = swap(a[j], a[j+1])
                #print(a[j], a[j+1])
                swap_count = swap_count+1
                #print('Swap count:', swap_count)
        #print('After pass', i, 'elements are: ', a)

    print('Array is sorted in',swap_count,'swaps.')
    #print('Sorted array: ', a)
    print('First Element:',a[0])
    print('Last Element:',a[-1])
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
sort_array(a,n)
