"""
Input: array of integers, target sum
Output: List of indices of the two numbers that sum to the target. 
Assume there is exactly one solution or none. You may not use the same element twice.

Runtime O(n)
"""

def two_sum(nums, target):
	"""
	One pass hash table implementation. Check if the complement is in the dictionary
	and return immediately if it is. Otherwise, add the current element to the dictionary.
	Dictionary key, value is number, index.
	"""
	ints = {}
	for i in range(len(nums)):
		complement = target - nums[i]
		if complement in ints:
			return [ints[complement], i] # return ints[complement] + [i]
		ints[nums[i]] = i # ints[nums[i]] = [i] is slightly faster but takes up more memory
