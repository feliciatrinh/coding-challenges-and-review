"""
Deterministically picks a better pivot. Better version of quickselect.
Worstcase runtime O(n)

1. Group the array into n/5 groups of 5 elements each (ignore any leftover elements)
2. Find the median of each group of 5 elements (as each group has a constant 5
elements, finding each individual median is O(1))
3. Create a new array with only the n/5 medians, and find the true median of this
array using Better-Quickselect.
4. Return this median as the chosen pivot
"""
