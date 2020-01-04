#Problem available at: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self,val):
        
        node = Node(val)
        if self.root == None:
            
            #print('Empty tree....')
            self.root = node
            node.left = node.right = None
            #print('Root',self.root.info)
        else:
            temp = self.root
            while(temp!=None):
                if (val <= temp.info):
                    #print('Left tree..')
                    if temp.left==None:
                        temp.left = node
                        node.left = None
                        #print('Root Left: ', self.root.left.info)
                        return self.root
                    else:
                        #print('Not None....')
                        temp = temp.left
        
                else:
                    #print('Right tree..')
                    if temp.right == None:
                        temp.right = node
                        node.right = None
                        #print('Root Right: ', self.root.right.info)
                        return self.root
                    else:
                        #print('Not None....')
                        temp = temp.right

        return self.root

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
