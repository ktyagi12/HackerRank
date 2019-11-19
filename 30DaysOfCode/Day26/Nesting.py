#Problem available at: https://www.hackerrank.com/challenges/30-nested-logic/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
def fine_calculate(actual_return_date,expected_return_date):
    fine = 0
    Da = int(actual_return_date[0])
    Ma = int(actual_return_date[1])
    Ya = int(actual_return_date[2])

    De = int(expected_return_date[0])
    Me = int(expected_return_date[1])
    Ye = int(expected_return_date[2])

    
    if(Ya>Ye):
        fine = 10000
    elif(Ya== Ye and Ma>Me):
        fine = 500 * (Ma-Me)
    elif(Ya == Ye and Ma == Me and Da>De):
        fine = 15 * (Da-De)
    else:
        fine = 0

    return fine
'''    
    if (Da <= De and Ma <= Me and Ya <= Ye):
        fine = 0
    elif(Da > De and Ma <= Me and Ya <= Ye):
        fine = 15 * (Da - De)
    elif(Ma > Me and Ya <= Ye):
        fine = 500 * (Ma - Me)
    elif(Ya>Ye):
        fine = 10000
    return fine

'''
actual_return_date = input().split()
expected_return_date = input().split()

fine=fine_calculate(actual_return_date,expected_return_date)
print(fine)
