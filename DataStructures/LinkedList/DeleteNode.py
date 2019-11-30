#Problem available at: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if(head == None):
        return
    elif(position == 0):
        head = head.next
    else:
        i = 0
        start = head
        while(i<(position-1)):
            start = start.next
            i=i+1
        if(start.next.next == None):
            start.next = None
        else:
            start.next = start.next.next

    return head

if __name__ == '__main__':