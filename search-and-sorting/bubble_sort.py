"""
Bubble Sort

Runtime: O(n^2)

- in-place and stable

Idea
- repeatedly swap adjacent elements until sorted
"""


def bubble_sort(lst):
    for i in range(0, len(lst) - 1):
        for j in range(1, len(lst)):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]

    return lst


assert bubble_sort([7, 2, 1, 8, 6, 3, 5, 4]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert bubble_sort([]) == []
assert bubble_sort([6, -1, 4, 10, 0, 0, -2]) == [-2, -1, 0, 0, 4, 6, 10]
assert bubble_sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
