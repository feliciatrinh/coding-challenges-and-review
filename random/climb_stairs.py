"""
Input: n number of steps. Positive number.
Output: ways to reach the top by taking either 1 or 2 steps at a time.

Runtime: O(n)

Solution is the nth + 1 Fib number.
Example: fib nums are 0, 1, 1, 2, 3
Input n = 1
output = 1

input n = 2
output = 2
"""


def climb_stairs(n):
	n += 1
	# don't need base cases b/c input n will always be >= 1
	prev = 0
	curr = 1
	for _ in range(2, n + 1):
		temp = curr
		curr = prev + curr
		prev = temp
	return curr
