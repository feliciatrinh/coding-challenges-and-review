"""
Input: head of singly linked list and integer value x
Output: linked list such that all nodes less than x come before all nodes greater than or equal to x

Runtime: O(n)
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def partition(head, x):
    curr = head
    less_front, less_last = None, None
    greater_front, greater_last = None, None

    while curr:
        if curr.val < x:
            if less_front:
                less_last.next = curr
                less_last = less_last.next
            else:
                less_front = curr
                less_last = curr
        else:
            if greater_front:
                greater_last.next = curr
                greater_last = greater_last.next
            else: 
                greater_front = curr
                greater_last = curr
        curr = curr.next
    if less_front:
        less_last.next = greater_front
        return less_front
    return greater_front
