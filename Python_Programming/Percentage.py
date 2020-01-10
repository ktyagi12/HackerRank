#Problem available at: https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen
def calc_perc(student_marks,query_name):
    if student_marks.__contains__(query_name):
        avg = 0
        val = student_marks[query_name]
        for i in val:
            avg = avg + i
        return (avg/len(val))
    else:
        return None


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg = calc_perc(student_marks,query_name)
    print(format(avg, '.2f'))
