#Problem available at: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem?h_r=next-challenge&h_v=zen

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
def heightOfTree(root):
    if root == None:
        return 0
    else:
        if (root.left == None and root.right == None):
            return 0
        else:
            return (1+max(heightOfTree(root.left),heightOfTree(root.right)))   

def printLevelWise(root,level):
    if root == None:
        return
    if level ==0:
        print(root.info, end = ' ')
    else:
        printLevelWise(root.left,level-1)
        printLevelWise(root.right,level-1)



def levelOrder(root):
    height = heightOfTree(root)
    for i in range(0,height+1):
        printLevelWise(root, i)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)