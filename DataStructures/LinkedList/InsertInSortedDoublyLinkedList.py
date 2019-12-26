#Problem available at: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    if(head==None):
        return
    node= DoublyLinkedListNode(data)
    start= head
    while(start!=None):
        if(start.next == None and start.prev == None):
            if(node.data>start.data):
                start.next=node
                node.prev= start
                return head
            else:
                node.next=start
                start.prev=node
                return head
        else:
            if node.data > start.data:
                if start.next == None:
                    start.next=node
                    node.prev = start    
                    return head
            else:
                if(start.prev==None):
                    node.next=start
                    start.prev=node
                    head = node
                    return head
                else:
                    start.prev.next= node
                    node.next = start
                    node.prev= start.prev
                    start.prev= node
                    return head
         
        start = start.next       
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()