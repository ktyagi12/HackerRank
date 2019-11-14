#Problem available at: https://www.hackerrank.com/challenges/30-interfaces/problem
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum_div = 0
        for i in range(1,n+1):
            if(n%i==0):
                sum_div = sum_div+i
    
        return sum_div


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)