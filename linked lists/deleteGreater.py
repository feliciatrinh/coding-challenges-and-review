"""
Input: head of a linked list
Output: head to the changed linked list

Given the head of a linked list and an integer x, delete all nodes
from the linked list with values greater than x.

Runtime: O(n)


"""


def deleteGreater(head, x):
	# Change the head pointer if the head contains a value greater than x.
	while head is not None and head.val > x: 
		head = head.next

	temp = head
	# Outer while loop is to traverse down the entire linked list
	while temp is not None:
		# Inner while loop is to traverse the linked list until we need to change pointers
		# Keep track of the previous node and the node at which its value exceeds x
		while temp is not None and temp.val <= x:
			prev = temp
			temp = temp.next
		# The current node's value is greater than x, so we skip over it.
		if temp is not None:
			prev.next = temp.next
			# re-assign temp to continue going down the linked list.
			temp = prev.next
		else: 
			return head
	return head


class Linkedlst(): 
    def __init__(self, head=None): 
        self.head = head

        
class Node(): 
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node