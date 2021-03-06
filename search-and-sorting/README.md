# Search and Sorting

## Sorting

* [Bubble Sort](bubble_sort.py)
	* Repeatedly swap adjacent elements until sorted.
	* Runtime: O(n^2)
* [Insertion Sort](insertion_sort.py)
	* Repeatedly swap the first unsorted element with its left neighbor while the left neighbor is greater than it until sorted.
	* Runtime: O(n^2)
* [Merge K Sorted Lists](merge_k_sorted.py)
	* Merge k sorted lists, each of length n into a single sorted list containing all k * n elements
	* Runtime: O(knlog(k))
	* Divide and conquer algorithm: sort each pair of k sorted lists using merge from mergesort recursively until only one list remains
* [Merge Sort](mergesort.py)
	* Sort an array by recursively splitting the array in half and merging the halves together.
	* Stable sorting method.
	* Runtime: O(nlogn)
* [Quick Sort](quicksort.py)
	* Sorts an array using a pivot
	* Unstable sorting method
	* Average runtime: O(nlogn), Worst-case runtime: (n^2)
* [Selection Sort](selection_sort.py)
	* Repeatedly swap the first unsorted element with the current minimum until sorted.
	* Runtime: O(n^2)

## Search

* [Binary Search](binary_search.py)
* [Count Occurrence](count_occurrence.py)
	* Return the number of occurrences of an integer in a sorted array.
	* Use binary search to find the first and last occurrence of n to take advantage of sortedness; see related problem [Find First and Last Position of Element in Sorted Array](first_last_position_sorted_array.py)
	* Runtime: O(logn)
* [Find First and Last Position of Element in Sorted Array](first_last_position_sorted_array.py)
    * Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
    * Uses binary search
    * Runtime: O(logn)
* [Kth Smallest](kth_smallest.py)
	* Given two sorted arrays of integers, each of size n, give the kth smallest element in sorted concatenation the
	two arrays.
	* Runtime: O(logk)
* [Max Difference](max_difference.py)
	* Returns the maximum difference between elements nums[j] and nums[i] where j > i.
	* Runtime: O(n)?
* [Median of Medians](median_of_medians.py)
	* Deterministically pick a better pivot for an algorithm like QuickSelect.
	* Runtime: O(n)
* [Median of Two Sorted Arrays](median_sorted_arrays.py)
	* Returns the median of two sorted arrays using the same idea as [Kth Smallest](kth_smallest.py).
	* Runtime: O(log(n + m))
* [Minimum Swaps](minimum_swaps.py)
	* Given an unordered array consisting of consecutive integers (1, 2,..., n) without any duplicates, find the minimum
	number of swaps required to sort the array in ascending order.
	* Runtime: O(n)
* [Quick Select](quickselect.py)
	* Given an array s of integers and an integer k, return the kth smallest element of s.
	* Average runtime: O(n), Worst-case runtime: O(n^2)
* [Search Rotated Sorted Array](search_rotated_sorted_array.py)
	* Given an array containing integers sorted in ascending order rotated about some pivot and an integer target,
	return the index of the target if found and -1 otherwise.
	* Runtime: O(logn) using binary search
