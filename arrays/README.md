# Arrays

* [Array Manipulation](array_manipulation.py)
    * Starting with a 1-indexed array of zeros and a 2D array of operations, for each operation add a value to each of
    the array elements between two given indices, inclusive. Once all operations have been performed, return the max
    value in your array.
    * Runtime: O(m) where m is the number of operations.
* [Beautiful Subarrays](beautiful_subarrays.py)
    * Return the number of subarrays containing m odd numbers.
    * Runtime: O(n) where n is the number of elements in the input array.
* [Circular Array](circular_array.py)
	* Given the number of nodes and a list of ending nodes (of length m) representing the paths taken, return the node
	that is visited the most.
	* Naive Solution Runtime: O(n * m) does not satisfy runtime requirement.
	* Optimal solution:
* [Consecutive Sum](consecutive_sum.py)
	* Given an int, find the number of ways to represent it as a sum of 2 or more consecutive integers.
	* Solution uses the arithmatic sum formula.
	* Runtime: linear with respect to the input integer?
* [Container with Most Water](container_with_most_water.py)
	* Given n non-negative integers a1, a2, ..., an , where each integer represents the height of a line; return the
	maximum possible area between any of two lines
	* Runtime: O(n)
* [Fibonacci](fibonacci.py)
	* Return the nth fibonacci number using an iterative, recursive, tail recursive solutions.
	* Worst runtime O(2^n), best runtime you usually see O(n)
* [K Difference](k_difference.py)
	* Given array of distinct integers, count the number of pairs of integers with difference k.
	* Runtime: O(n)
* [Overlapping Region Grid Game](overlapping_region_grid_game.py)
	* Given a list of n lists in which each of the n lists is a pair of integers a and b, return the total number of
	occurrences of the greatest integer x in the grid after n steps
	* Runtime: O(n)
* [Search Rotated Sorted Array](search_rotated_sorted_array.py)
	* Given an array containing integers sorted in ascending order rotated about some pivot and an integer target,
	return the index of the target if found and -1 otherwise.
	* Runtime: O(logn) using binary search
* [Spiral Order](spiral_order.py)
	* Given a 2D matrix, return the spiral pattern as a flat array.
	* Runtime: O(nm)
* [Sum to K](sum_to_k.py)
	* Given an array of integers (not necessarily distinct), return the number of pairs that sum to k.
	* Runtime: O(n)
* [Three Sum](three_sum.py)
	* Given an array of n integers, return a list of all unique triplets that sum to 0.
	* Uses logic from the [Two Sum problem](two_sum.py) and itertools.groupby()
	* Runtime: O(n^2)
	* See the related problem [Three Sum Closest](three_sum_closest.py)
* [Triple Product](tripleProduct.java)
	* Given an array of positive and negative numbers, return the maximum possible product of 3 numbers.
	* Runtime: O(n)
* [Two Sum](two_sum.py)
	* Given an array of integers and a target, return the indices of the two numbers that sum to the target.
	* Runtime: O(n)

## Less Relevant Problems
* [Bone Trousle](bonetrousle.py)
    * Given the values of n, k, and b for trips to the store, determine which boxes Papyrus must purchase during each
    trip. He purchases exactly b boxes, has k boxes availble at the store where each box contains k sticks, wants n
    sticks total. Outputs one possible solution.
    * Runtime: O(b)?
* [Counting Valleys](counting_valleys.py)
	* From HackerRank
* [Cut Bamboo](cut_bamboo.py)
	* Given an array of integer lengths, return an array of integers where each represents the number of pieces at the
	start of each turn.
	* Runtime: worstcase O(n^2) when the lengths differ by 1 (e.g. [1, 2, 3, 4, 5...])
* [Hour Glass Sum](hour_glass_sum.py)
	* Return the maximum hourglass sum in a 2D array. An hourglass in A is a subset of values with indices falling in an
	hourglass pattern.
* [Jumping on Clouds](jumping_on_clouds.py)
	* Return the minimum number of jumps it'll take Emma to jump from her starting position to the last cloud.
* [Minimum Bribes](minimum_bribes.py)
* [No Duplicates](no_duplicates.py)
* [Rectangles](rectangles.py)
	* Given a 2D array filled with 1s and 0s, find the starting and end point of all rectangles filled with 0.
	* Runtime: O()
* [Rotate Left](rot_left.py)
	* Shift each element d units to the left.
* [Sock Merchant](sock_merchant.py)
* [Three Sum Closest](three_sum_closest.py)
	* Given an array nums of n integers and an integer target, return the sum of three integers in nums that is closest
	to target.
	* Runtime: best case O(n^2) and worst case O(n^3)?