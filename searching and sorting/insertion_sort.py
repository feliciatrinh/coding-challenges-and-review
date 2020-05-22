"""
Insertion Sort

Runtime: O(n^2)
- Best runtime of O(n) when list is already sorted

- in-place and stable

- partition list into sorted section and unsorted section; initially mark the first element as sorted
- for the rest of the unsorted elements, keep swapping the element with its left neighbor while the left neighbor is
  greater than the element
- repeat until sorted
"""


def insertion_sort(lst):
    if not lst:
        return lst

    for i in range(1, len(lst)):
        curr = lst[i]
        j = i
        while j > 0 and lst[j - 1] > curr:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1

    return lst


assert insertion_sort([7, 2, 1, 8, 6, 3, 5, 4]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert insertion_sort([]) == []
assert insertion_sort([6, -1, 4, 10, 0, 0, -2]) == [-2, -1, 0, 0, 4, 6, 10]
assert insertion_sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
