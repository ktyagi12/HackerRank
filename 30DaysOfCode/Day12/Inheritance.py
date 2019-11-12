#Problem available at: https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
        def __init__(self, firstName,lastName,idNum,scores):
            Person.__init__(self, firstName, lastName, idNum)
            self.scores = scores   
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
        def calculate(self):
            sum_all = 0
            avg = 0
            for i in self.scores:
                sum_all = sum_all + i
            avg = sum_all/len(self.scores)
            if avg<40:
                return 'T'
            elif avg <55:
                return 'D'
            elif avg<70:
                return 'P'
            elif avg<80:
                return 'A'
            elif avg<90:
                return 'E'
            else:
                return 'O'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())