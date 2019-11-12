#Problem available at: https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = 0
        max_num = max(self.__elements)
        min_num = min(a)
        self.maximumDifference = abs(max_num- min_num)

    # Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)