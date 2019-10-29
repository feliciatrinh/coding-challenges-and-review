"""
Input: head to linked list containing 0's and 1's
Output: Unsigned decimal representation of the binary number represented by this linked list

Example: 
Input: head -> 0 -> 1 -> 1 -> null
Output: 3

Solution: Add the value of each node into a list in reverse, iterate through the list at the end to calculate the decimal value
Runtime: O(n)
"""


def binary(head):
	count = 0
	decimal = 0
	values = []
	while head is not None:
		# insert the values of each node into a list in reverse order
		values.insert(0, head.val)
		count += 1
		head = head.next
	for i in range(count):
		# calculate the decimal representation of the binary number
		decimal += values[i] * 2**i
	return decimal


class Linkedlst(): 
    def __init__(self, head=None): 
        self.head = head

        
class Node(): 
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node