"""
Input: head to linked list containing 0's and 1's
Output: Unsigned decimal representation of the binary number represented by this linked list

Runtime: O(n)

Example: 
Input: head -> 0 -> 1 -> 1 -> null
Output: 3

Idea
Add the value of each node into a list in reverse, iterate through the list at the end to calculate the decimal value
"""


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def binary(head):
    values = []
    while head is not None:
        values.insert(0, head.val)
        head = head.next

    decimal = 0
    for i, val in enumerate(values):
        decimal += val * 2**i
    return decimal


lst = Node(0, Node(1, Node(1)))
assert binary(lst) == 3
