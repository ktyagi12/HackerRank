#Problem available at: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    input_list = list(arr)
    input_list.sort()
    out_list = []

    for i in input_list:
        if i not in out_list:
            out_list.append(i)

    print(out_list[-2])
