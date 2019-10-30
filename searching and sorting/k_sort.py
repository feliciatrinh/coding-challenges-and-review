"""
Input: list of k sorted arrays
Output: one sorted array

Runtime: O(nk * logk)

Ex:
input: [[5, 7, 8], [1, 2, 3], [10, 12, 14]]
output: [1, 2, 3, 5, 7, 8, 10, 12, 14]

Use divide and conquer alg. Pair up the k
"""

def k_sort(lst):
	if len(lst) <= 1:
		return lst[0]
	new_lst = []
	for i in range(0, len(lst), 2):
		new_lst.append(merge(lst[i], lst[i + 1]))
	if len(lst) % 2 != 0:
		new_lst.append(lst[-1])
	k_sort(new_lst)

def merge(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    elif lst1[0] <= lst2[0]:  # use <= for stable sorting
        return [lst1[0]] + merge(lst1[1:], lst2)
    return [lst2[0]] + merge(lst1, lst2[1:])
	