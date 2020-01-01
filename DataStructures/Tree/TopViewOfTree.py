#Problem available at: https://www.hackerrank.com/challenges/tree-top-view/problem

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def topView(root):    
    if(root==None):
        return
    elif(root.left == root.right==None):
        print(root.info,end= ' ')
    else:
        d={};q=[root];hd=0;root.level=hd
    while len(q)>0:
            root=q.pop(0)
            hd=root.level
            if hd not  in d:
                d[hd]=root.info
            if root.left!=None:
                root.left.level=hd-1
                q.append(root.left)
            if root.right!=None:
                root.right.level=hd+1
                q.append(root.right)  
    for i in sorted(d):
        print(d[i],end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)