"""
Input: integer num
Output: The number of ways to represent num as a sum of 2 or more consecutive integers

Given a long int, find the number of ways to represent it as a sum of 2 or more consecutive integers.

Solution: Use the arithmatic sum formula to determine which integers you can start at.
Runtime: linear?

Example: 
Input: 15
1, 2, 3, 4, 5
4, 5, 6
7, 8

Output: 3 ways 
"""


def consecutive_sum(num):
	# summing consecutive integers is start + (start + 1) + (start + 2) + ... + (start + end)
	# requires 2 or more consecutive integers, so I start with end = 1
	end = 1
	count = 0
	# in the summation above, we have 1 + 2 + ... + end = end * (end + 1) / 2 by arithmatic sequence formula
	# we don't need to consider any more integers once this sum equals num because any sum
	# of consecutive integers beyond this starting point will exceed num
	while end * (end + 1) / 2 < num:
		start = (2.0 * num - end * (end + 1))/(2.0 * (end + 1))
		# check if our possible start is a positive integer
		if start > 0 and start.is_integer():
			count += 1
		end += 1
	return count
