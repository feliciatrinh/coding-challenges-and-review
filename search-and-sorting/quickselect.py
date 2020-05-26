"""
Input: a list of numbers s; an integer k
Output: the kth smallest element of s

Quickselect alg for finding the kth smallest element in an unsorted array
picks an arbitrary pivot then partitions the array into 3 pieces:
elements less than the pivot, elements equal to the pivot, elements greater than pivot. 
It is then recursively called on the piece of the array
that still contains the kth smallest element.

1 <= k <= len(s)
k = 1 corresponds to the minimum of s

- pick a random pivot
- average runtime O(n)
- worst case runtime O(n^2)
"""
from random import choice


def quickselect(s, k):
    if not s:
        return None
    v = choice(s)  # pivot selection
    s_l, s_v, s_r = [], [], []  # less than, equal to, and greater than subarrays
    for elem in s:
        if elem < v:
            s_l.append(elem)
        elif elem == v:
            s_v.append(elem)
        else:
            s_r.append(elem)
    if len(s_l) >= k:
        return quickselect(s_l, k)
    elif len(s_l) + len(s_v) >= k:
        return v
    else:
        return quickselect(s_r, k - len(s_l) - len(s_v))
