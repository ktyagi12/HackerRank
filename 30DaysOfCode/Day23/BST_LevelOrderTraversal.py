#Problem available at: https://www.hackerrank.com/challenges/30-binary-trees/problem

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def heightOfTree(self,root):
        if root == None:
            return 0
        else:
            if (root.left == None and root.right == None):
                return 0
            else:
                return (1+max(self.heightOfTree(root.left),self.heightOfTree(root.right)))    

    def printLevelWise(self,root,level):
        if root == None:
            return
        if level ==0:
            print(root.data, end = ' ')
        else:
            self.printLevelWise(root.left,level-1)
            self.printLevelWise(root.right,level-1)



    def levelOrder(self,root):
        height = self.heightOfTree(root)
        for i in range(0,height+1):
            self.printLevelWise(root, i)

        #Write your code here

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)