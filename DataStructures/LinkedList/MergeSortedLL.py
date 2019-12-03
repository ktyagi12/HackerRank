#Problem available at: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
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

def mergeLists(head1, head2):
    if(head1 == None and head2 == None):
        return
    elif(head1== None):
        return head2
    elif(head2 == None):
        return head1
    else:
        s1= head1
        s2 = head2
        s3 = SinglyLinkedList()

        while(s1!=None and s2!=None):
            if(s1.data <s2.data):
                s3.insert_node(s1.data)
                s1 = s1.next
            elif(s1.data > s2.data):
                s3.insert_node(s2.data)
                s2 = s2.next
            else:
                s3.insert_node(s1.data)
                s1 = s1.next
                s3.insert_node(s2.data)
                s2 = s2.next
            
        if(s1 == None):
            s3.tail.next = s2 
        else:
            s3.tail.next = s1 

    return s3.head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
