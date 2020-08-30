"""
Source: Leetcode

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

Best Runtime: O(logn)
Space complexity: O(n)

Ideas
- Sort array when median is needed
    - when a new element comes in, add the element to the end of the resizable array
    - when you need to find the median, sort the array and return the middle element or the average of the two middle
    elements
    - O(nlogn) for sorting, O(1) for finding the median
    - space complexity: O(n)

- always keep the array sorted
    - when a new element comes in, add the element to the already sorted array where it needs to be for the array to
      maintain sortedness
    - put new element in array, shift everything else
    - O(n) for scanning the array insertion sort and shifting the rest of the elements?
    - runtime exceeded

    - because array is always sorted, could use binary search to find the index where you'd insert the new element
    - run time would still be O(n) on average for shifting the rest of the elements?
    - runtime passed

- Use 2 heaps
    - keep a max heap of the smaller half of elements and a min heap of larger half of elements, approx. equal sizes
    - when the min heap is becoming too large (i.e. size(min_heap) - size(max_heap) > 1),
      pop off the top of the min heap and add it to the max heap
        - to avoid constantly having to compare our num to the tops of each heap, we can maintain that the min_heap
          contains n + 1 elements while the max_heap contains n elements whenever there is an odd number of elements
        - to do this: when the two sizes are the same, push the new element into the max_heap.
          pop the top of the max_heap and push it into the min_heap
        - when the sizes aren't the same, push the new element into the min_heap.
          pop the top of the min_heap and push it into the max_heap
    - the median will be the top of the larger heap or the average of the top of both heaps so O(1)
    - O(logn) for re-ordering/inserting into the heaps
    documentation for built-in min heap: https://docs.python.org/3.8/library/heapq.html

- self balancing BST like a red-black/AVL tree
    - the median of a BST is always the root or the average of the root and one of the root's children

TODO: look up reservoir sampling implementation from CS170
"""


class MedianFinderSortWhenNeeded:

    def __init__(self):
        self.data = []

    def add_num(self, num: int) -> None:
        self.data.append(num)

    def find_median(self) -> float:
        """
        :return: median of data stream in O(nlogn) time
        """
        self.data.sort()
        length = len(self.data)
        mid = length // 2
        if length % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]


class MedianFinderKeepSorted:

    def __init__(self):
        self.data = []

    def add_num(self, num: int) -> None:
        for i in range(len(self.data)):
            if num < self.data[i]:
                self.data.insert(i, num)
                return
        self.data.append(num)

    def add_num_binary_search(self, num: int) -> None:
        def binary_search(lo, hi):
            if lo > hi:
                return lo
            mid = (lo + hi) // 2
            if num == self.data[mid]:
                return mid
            if num < self.data[mid]:
                return binary_search(lo, mid - 1)
            if num > self.data[mid]:
                return binary_search(mid + 1, hi)

        self.data.insert(binary_search(0, len(self.data) - 1), num)

    def find_median(self) -> float:
        """
        :return: median of data stream in O(n) time
        """
        length = len(self.data)
        mid = length // 2
        if length % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]


class MedianFinderHeaps:

    def __init__(self):
        self.max_heap = []  # smaller half
        self.min_heap = []  # larger half

    def add_num(self, num: int) -> None:
        import heapq
        # heappushpop pushes num onto heap, then pops and returns smallest item from the heap
        if len(self.max_heap) == len(self.min_heap):
            # heappq heaps are min heaps by default, negative the num to get a max heap
            # negate it again to correct the input to the min heap
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def find_median(self) -> float:
        """
        :return: median of data stream in O(logn) time
        """
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return self.min_heap[0]


median_finder = MedianFinderSortWhenNeeded()
median_finder.add_num(1)
median_finder.add_num(2)
assert median_finder.find_median() == 1.5
median_finder.add_num(3)
assert median_finder.find_median() == 2

median_finder = MedianFinderKeepSorted()
median_finder.add_num(1)
median_finder.add_num(2)
assert median_finder.find_median() == 1.5
median_finder.add_num(3)
assert median_finder.find_median() == 2

median_finder = MedianFinderKeepSorted()
median_finder.add_num(1)
median_finder.add_num(3)
assert median_finder.find_median() == 2
median_finder.add_num(2)
assert median_finder.find_median() == 2

median_finder = MedianFinderKeepSorted()
median_finder.add_num_binary_search(1)
median_finder.add_num_binary_search(3)
assert median_finder.find_median() == 2
median_finder.add_num_binary_search(2)
assert median_finder.find_median() == 2

median_finder = MedianFinderHeaps()
median_finder.add_num(1)
median_finder.add_num(3)
assert median_finder.find_median() == 2
median_finder.add_num(2)
assert median_finder.find_median() == 2
