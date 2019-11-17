#Problem available at: https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def removeDuplicates(self,head):
        if head == None:
            #print('Empty list...')
            return
        elif(head.next == None):
            #print('Only one element in the list..')
            return head                 
        else:
            #print('More than 1 element in the list..')
            start = head
            while(start.next!=None):
                if start.data == start.next.data and start.next.next!=None:
                    #print('Duplicate found..')
                    start.next= start.next.next
                elif start.data == start.next.data and start.next.next==None:
                    start.next= None
                    return head
                else:
                    start= start.next
            return head



mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 