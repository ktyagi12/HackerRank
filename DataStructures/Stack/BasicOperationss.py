#Problem available at: https://www.hackerrank.com/challenges/maximum-element/problem

def push_ele(stack_list,ele,max_ele):
    if (max_ele < ele):
        max_ele = ele
    stack_list.append(ele)
    #print('Max: and list: ', max_ele, stack_list)
    return max_ele

def pop_ele(stack_list,max_ele):
    if len(stack_list) == 0:
        return
        #print('Empty Stack..')
    else:
        ele = stack_list.pop(-1)
        #print('Popped element: ',ele)
        if (ele == max_ele and len(stack_list) == 0):
            max_ele = 0
        elif(ele == max_ele and len(stack_list) > 0 ):
            max_ele = max(stack_list)
            #print('After pop: ', stack_list)
        return max_ele


n = int(input())
stack_list = []
max_ele = 0

for i in range(n):
    query = list(map(str, input().split()))
    #print('Query: ', query)
    query_type = int(query[0])
    #print('Query type: ', query_type)

    if query_type == 1:
        ele = int(query[1])
        #print('Ele: ', ele)
        max_ele = push_ele(stack_list, ele, max_ele)
    

    elif query_type == 2:
        max_ele = pop_ele(stack_list, max_ele)
    

    elif query_type == 3:
        print(max_ele)