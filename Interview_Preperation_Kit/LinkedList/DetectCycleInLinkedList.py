#Problem available at: https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if(head==None):
        return False
    elif(head.next==None):
        return False
    else:
        start= head
        while(1):
            if start.next==None:
                return False
            if start.next.data=='NA':
                return True
            else:
                start.data= 'NA'
                start=start.next
        return False