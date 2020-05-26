"""
Source: Leetcode
Input: singly linked list
Output: boolean True if linked list is a palindrome, False otherwise

Runtime: O(n)
Space Complexity: O(n)

Naive
Runtime: O(n)
Space: O(n)
- create a copy of the linked list and reverse it then compare the first half of the nodes of the original linked list 
  and the first half of the nodes of the reversed linked list
- if you reach None then return True

Better
Runtime: O(n)
Space: O(1)
- Reverse the first half of the linked list in-place. Use two pointers to compare each pair of nodes starting from the midpoint
  to the ends of the linked list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    """
    Return the reversed linked list as a new linked list and half the length of the linked list.
    """
    length = 0
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr_in_new_linked_lst = ListNode(curr.val, prev)
        prev = curr_in_new_linked_lst
        curr = next_node
        length += 1
    return prev, length // 2


def palindrome_linked_list_reverse(head):
    """
    Compare half of the original linked list with half of the reversed linked list.
    Space complexity: O(n)
    """
    head_reversed, i = reverse(head)

    while i > 0 and head.val == head_reversed.val:
        i -= 1
        head = head.next
        head_reversed = head_reversed.next
    return not i


lst1 = ListNode(1, ListNode(2))
lst2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

assert palindrome_linked_list_reverse(lst1) == False
assert palindrome_linked_list_reverse(lst2) == True
