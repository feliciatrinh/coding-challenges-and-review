"""
Source: Leetcode
Input: singly linked list
Output: boolean True if linked list is a palindrome, False otherwise

Runtime: O(n)
Space Complexity: O(1)

Naive
Runtime: O(n)
Space: O(n)
- create a copy of the linked list and reverse it then compare the first half of the nodes of the original linked list 
  and the first half of the nodes of the reversed linked list
- Alternatively, you could use a stack instead of creating a new linked list

Better?
Runtime: O(n)
Space: O(1)
- Reverse the first half of the linked list in-place. Use two pointers to compare each pair of nodes starting from the midpoint
  to the ends of the linked list
- make sure to ignore the middle node if there is an odd number of nodes in the linked list
- make sure to restore the original linked list if required
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


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


def palindrome_linked_list_alt(head):
    """
    Source: Leetcode
    Reverse the first half of the linked list in place and compare with the second half.
    Restores the half reversed linked list to its original state at the end.
    """
    def reverse_half(head_ptr, half_length):
        """
        Reverses the first half of the linked list in-place.
        """
        prev = None
        curr = head_ptr
        while half_length > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            half_length -= 1
        return prev, curr

    def restore_linked_list(left_head, right_head):
        """
        Restores a half-reversed linked list to its original state.
        """
        curr = left_head
        prev = right_head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

    length = 0
    temp_node = head
    while temp_node is not None:
        length += 1
        temp_node = temp_node.next

    left_ptr, right_ptr = reverse_half(head, length // 2)
    left, right = left_ptr, right_ptr

    if length % 2 != 0:
        right = right.next

    while left is not None or right is not None:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    restore_linked_list(left_ptr, right_ptr)
    return True


lst1 = ListNode(1, ListNode(2))
lst2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
lst3 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))

assert palindrome_linked_list_reverse(lst1) is False
assert palindrome_linked_list_reverse(lst2) is True
assert palindrome_linked_list_reverse(lst3) is True

assert palindrome_linked_list_alt(lst1) is False
assert palindrome_linked_list_alt(lst2) is True
assert palindrome_linked_list_alt(lst3) is True
