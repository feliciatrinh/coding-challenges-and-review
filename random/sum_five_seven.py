"""
Input: n
Output: sum of numbers between 1 and n, inclusive, that aren't divisible by 5 or 7.
Runtime: O(n)

Example:
input n = 10
output = 33
"""


def naive_sum(n):
	"""
	Add each number that isn't divisible by 5 or 7 to the running sum.
	Runtime: O(n)
	"""
	count = 0
	for i in range(n + 1):
		if i % 5 != 0 and i % 7 != 0:
			count += i
	return count


def sum_formula(n):
	"""
	Uses the arithmetic sum formula to make small inputs constant time.
	Summation of 1 to n = n * (n + 1) / 2
	"""
	count = n * (n + 1) / 2
	if n >= 5:
		for i in range(5, n + 1, 5):
			count -= i
	if n >= 7:
		for i in range(7, n + 1, 7):
			count -= i
	return count
