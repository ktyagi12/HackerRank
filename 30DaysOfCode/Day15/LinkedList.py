#Problem available at: https://www.hackerrank.com/challenges/30-linked-list/problem
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        node = Node(data)
        if (head == None):
            self.head = node
            return self.head
        elif (self.head.next == None):
            self.head.next = node
        #self.node.next = None
            return self.head
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = node
            return self.head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 