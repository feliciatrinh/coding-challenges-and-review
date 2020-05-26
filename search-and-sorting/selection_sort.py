"""
Selection Sort

Runtime: O(n^2)

- in-place and stable

Idea
- set the first unsorted element as the minimum
- iterate through the unsorted elements and find the new minimum
- swap the minimum with the first unsorted position
"""


def selection_sort(lst):
    for i in range(0, len(lst)):
        minimum = lst[i]
        min_ind = i
        for j in range(i + 1, len(lst)):
            if lst[j] < minimum:
                minimum = lst[j]
                min_ind = j
        lst[i], lst[min_ind] = minimum, lst[i]

    return lst


assert selection_sort([7, 2, 1, 8, 6, 3, 5, 4]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert selection_sort([]) == []
assert selection_sort([6, -1, 4, 10, 0, 0, -2]) == [-2, -1, 0, 0, 4, 6, 10]
assert selection_sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
