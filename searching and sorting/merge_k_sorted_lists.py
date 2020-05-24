"""
Source: CS 170, Spring 2019 UC Berkeley
Input: k sorted lists, each of length n
Output: a single sorted list containing the elements of all the lists

Assumes input can't be an empty list.

Runtime: O(knlog(k))

Divide and Conquer Alg

Idea 1
- Call the algorithm recursively on the first k/2 sorted lists, then on the second k/2 sorted lists.
- Then merge them together (this takes kn/2 time). The recurrence is T(k) = 2T(k/2) + O(kn).
- This gives time kn + 2(k/2)n + . . . + 2^(log k)(k/2^(log k))n = O(kn log k) b/c there are log(k) levels and you do
  a total of k*n comparisons per level.

Idea 2
- Do the k-way merge all at once. 
- Keep a pointer to the start of each array.
- Add the smallest element in each array to a heap.
- Repeatedly pull the smallest item from the heap and increment the pointer of the array it came
from. Then add the destination of the pointer to the heap. Do this until the heap is empty and
all pointers point past their arrays.
- This is kn heap operations (delete, insert) on a heap of size at most k, giving time O(kn log k).

Idea 3
- Similar to the above, put the smallest elements from each array into a new k-length array A and
sort them. Keep a pointer to the start of each array.
- Repeatedly pull the smallest element from A, increment the pointer it came from. Use binary
search to insert the destination of the pointer into the right place into A. Do this until the array
is empty and all pointers point past their arrays.
- It is not obvious how to implement this, as you need an array with constant-time seek and insert
operations. If you use an amortized data-structure, you will get O(kn log k) as well.

It is not enough to merge the first two lists, then merge the result with the third, then the result with
the fourth, etc. This would give a k^2log n runtime.
"""


def merge_k_sorted(lst):
    """
    Idea 1, basically merge sort
    """
    def merge(lst1, lst2):
        """
        Merge two sorted lists into a single sorted list.
        """
        if not lst1:
            return lst2
        elif not lst2:
            return lst1
        elif lst1[0] <= lst2[0]:  # use <= for stable sorting
            return [lst1[0]] + merge(lst1[1:], lst2)
        return [lst2[0]] + merge(lst1, lst2[1:])

    if len(lst) <= 1:
        return lst[0]

    return merge(merge_k_sorted(lst[:len(lst) // 2]), merge_k_sorted(lst[len(lst) // 2:]))

assert merge_k_sorted([[1, 3, 5], [2, 7, 9], [-1, 20, 100]]) == [-1, 1, 2, 3, 5, 7, 9, 20, 100]
assert merge_k_sorted([[2, 5, 7], [1, 4, 10], [8, 10, 12], [0, 3, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 12]


def merge_k_sorted_heap(lst):
    pass