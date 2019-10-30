# Search and Sorting

* [Count Occurrence](countOccurrence.py)
	* Return the number of occurrences of an integer in a sorted array in O(logn) time.
	* Use binary search to find the first and last occurrence of n to take advantage of sortedness.
	* TODO: Fix your solution.
* [K Sort](k_sort.py)
	* Return k sorted lists as a single sorted list
	* Runtime: O(n * logk)
	* Divide and conquer algorithm: sort each pair of k sorted lists using merge from mergesort recursively until only one list remains
* [Kth Smallest](kth_smallest.py)
	* Given two sorted arrays of integers, each of size n, give the kth smallest element in the union of the two arrays.
	* Runtime O(logk)
* [Max Difference](maxDifference.py)
	* Returns the maximum difference between elements nums[j] and nums[i] where j > i.
	* Runtime O(n)?
* [Median of Medians](median_of_medians.py)
	* Deterministically pick a better pivot for an algorithm like QuickSelect.
	* Runtime O(n)
* [Merge Sort](mergesort.py)
	* Sort an array by recursively splitting the array in half and merging the halves together.
	* Stable sorting method.
	* Runtime O(nlogn)
* [Minimum Swaps](minimumSwaps.py)
	* Given an unordered array consisting of consecutive integers (1, 2,..., n) without any duplicates, find the minimum number of swaps required to sort the array in ascending order.
	* Runtime O(n)
* [Quick Select](quickselect.py)
	* Given an array s of integers and an integer k, return the kth smallest element of s.
	* Average runtime O(n), worst case runtime O(n^2)
* [Quick Sort](quicksort.py)
	* Sorts an array using the first element as the pivot.
	* Unstable sorting method.
	* Average runtime O(nlogn), worstcase (n^2)