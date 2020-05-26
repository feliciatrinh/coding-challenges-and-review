"""
Input: l1: ListNode, l2: ListNode
Output: ListNode of the sum of l1 and l2 where the digits are stored in reverse

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Runtime: O(n)
Source: Leetcode

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8 b/c 342 + 465 = 807
"""


class Node:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


def add_two_numbers(l1, l2):
    """
    Solution that uses modulo 10 to get the last digit and flooring
    to go to the next digits place. In this solution, you don't have
    to worry about carrying over.
    Faster average runtime than the 2nd solution but not by much.
    """
    total = 0
    i = 1
    while l1 is not None or l2 is not None:
        if l1 is not None:
            total += l1.val * i
            l1 = l1.next
        if l2 is not None:
            total += l2.val * i
            l2 = l2.next
        i *= 10
    if total == 0:
        return Node(0)
    head = Node(total % 10)
    curr = head
    total = total // 10
    while total != 0:
        curr.next = Node(total % 10)
        total = total // 10
        curr = curr.next
    return head


def add_two_numbers_alt(l1, l2):
    """
    Solution that builds to resultant linked list as you go through
    each digit in l1 and l2.
    """
    result = Node((l1.val + l2.val) % 10)
    carry = (l1.val + l2.val) // 10
    curr = result
    l1 = l1.next
    l2 = l2.next
    while l1 is not None or l2 is not None:
        tot = 0
        if l1 is not None:
            tot += l1.val
            l1 = l1.next
        if l2 is not None:
            tot += l2.val
            l2 = l2.next
        tot += carry
        curr.next = Node(tot % 10)
        carry = tot // 10
        curr = curr.next
    if carry != 0:  # could have one last carry over
        curr.next = Node(carry)
    return result
