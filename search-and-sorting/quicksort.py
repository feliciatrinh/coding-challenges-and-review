"""
Quick sort
Input: unsorted list (could possibly be sorted)
Output: sorted list

- Quick sort is NOT stable, unlike mergesort

Average runtime: O(nlogn)
- when you have a good pivot, e.g. the median
Worst case runtime: O(n^2)
- algorithm becomes selection sort when your pivot is the smallest element or the largest element and the input is
  already sorted

Lomuto Partition Scheme (source: Wikipedia, stackoverflow)
- worst-case runtime when the list is already in order
- choose a pivot, usually the last element
- maintain an index i as you scan the list using another index j s.t. the elements at lo through i-1 (inclusive) are
  less than the pivot and elements i through j (inclusive) are greater than or equal the pivot
- partition() helper function returns the index i, around which you recursively sort the partitioned list b/c now
  all elements to the left of i should be less than lst[i] and all elements to the right of i should be greater than or
  equal to lst[i]
- sort the entire input list by returning lomuto_quicksort(lst, 0, len(lst) - 1)
- less efficient than Hoare partition scheme

Hoare Partition Scheme (source: Wikipedia)
- use two pointers: each pointer points to one end of the list
- the pointers move inward until they detect an inversion: a pair of elements (one greater than or equal to the pivot,
  one less than or equal to the pivot) that are in the wrong order relative to each other
- the algorithm stops and returns the final index when the two pointers meet or pass each other
- partition() helper function returns the index j, around which you recursively sort the partitioned list b/c now all
  elements to the left of and including j are less than or equal to the pivot and all elements to the right of j are
  greater than the pivot
- more efficient than Lomuto partition scheme b/c does 3 fewer swaps on average
"""


def lomuto_quicksort(lst):
    """
    In-place quick sort using the Lomuto Partition Scheme.
    """
    def quicksort(lst, lo, hi):
        if lo < hi:  # sorting is in-place, so lst should already be sorted otherwise
            p = partition(lst, lo, hi)
            quicksort(lst, lo, p - 1)  # sort the left partition
            quicksort(lst, p + 1, hi)  # sort the right partition

    def partition(lst, lo, hi):
        pivot = lst[hi]
        i = lo
        for j in range(lo, hi):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        # all elements to the left of i are less than the pivot. This doesn't include the element at i, so we need to
        # swap it with the pivot
        lst[i], lst[hi] = lst[hi], lst[i]
        return i

    quicksort(lst, 0, len(lst) - 1)
    return lst


def hoare_quicksort(lst):
    """
    In-place quick sort using the Hoare Partition Scheme.
    """
    def quicksort(lst, lo, hi):
        if lo < hi:  # sorting is in-place, so lst should already be sorted otherwise
            p = partition(lst, lo, hi)
            quicksort(lst, lo, p)
            quicksort(lst, p + 1, hi)

    def partition(lst, lo, hi):
        pivot = lst[(lo + hi) // 2]
        i = lo
        j = hi
        while True:
            while lst[i] < pivot:
                i += 1

            while lst[j] > pivot:
                j -= 1

            if i >= j:  # the two pointers meet or pass each other
                return j

            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    quicksort(lst, 0, len(lst) - 1)
    return lst


def quicksort(lst):
    """
    Quick sort that reqs additional memory and always uses the first element as the pivot.
    Space complexity: O(n)
    """
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    less = [item for item in lst[1:] if item < pivot]
    equal = [pivot] + [item for item in lst[1:] if item == pivot]
    greater = [item for item in lst[1:] if item > pivot]
    return quicksort(less) + equal + quicksort(greater)


assert quicksort([5, 10, 2, 1, 0, 1, 5]) == [0, 1, 1, 2, 5, 5, 10]
assert quicksort([]) == []
assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert quicksort([1, 1, 1, 1]) == [1, 1, 1, 1]

assert lomuto_quicksort([5, 10, 2, 1, 0, 1, 5]) == [0, 1, 1, 2, 5, 5, 10]
assert lomuto_quicksort([]) == []
assert lomuto_quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert lomuto_quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert lomuto_quicksort([1, 1, 1, 1]) == [1, 1, 1, 1]

assert hoare_quicksort([7, 2, 1, 8, 6, 3, 5, 2, 4, 8]) == [1, 2, 2, 3, 4, 5, 6, 7, 8, 8]
assert hoare_quicksort([]) == []
assert hoare_quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert hoare_quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert hoare_quicksort([1, 1, 1, 1]) == [1, 1, 1, 1]
