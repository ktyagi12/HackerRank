#Problem available at: https://www.hackerrank.com/challenges/nested-list/problem
def sec_lowest(students):
    if len(students)== 0 :
        return None
    students.sort(key = lambda k: k[1])
    min_marks = students[0][1]
    for i in students:
        if min_marks < i[1]:
            min_marks = i[1]
            break
    a = [x[0] for x in students if x[1] == min_marks]
    a.sort()
    for i in a:
        print(i)


if __name__ == '__main__':
    students = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    sec_lowest(students)