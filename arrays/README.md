# Arrays

* [Array Manipulation](arrayManipulation.py)
    * Starting with a 1-indexed array of zeros and a 2D array of operations, for each operation add a value to each of the array elements between two given indices, inclusive. Once all operations have been performed, return the max value in your array.
    * Runtime: O(m) where m is the number of operations.
* [Beautiful Subarrays](beautifulSubarrays.py)
    * Return the number of subarrays containing m odd numbers.
    * Runtime: O(n) where n is the number of elements in the input array.
* [Circular Array](circular_array.py)
	* Given the number of nodes and a list of ending nodes representing the paths taken, return the node that is visited the most.
	* Naive solution does not satisy runtime requirement.
	* Optimal solution:
* [Consecutive Sum](consecutive_sum.py)
	* Given an int, find the number of ways to represent it as a sum of 2 or more consecutive integers.
	* Solution uses the arithmatic sum formula.
	* Runtime: linear with respect to the input integer?
* [Cut Bamboo](cut_bamboo.py)
	* Given an array of integer lengths, return an array of integers where each represents the number of pieces at the start of each turn.
	* Runtime: worstcase O(n^2) when the lengths differ by 1 (e.g. [1, 2, 3, 4, 5...]) 
* [Fibonacci](fibonacci.py)
	* Return the nth fibonacci number using an iterative, recursive, tail recursive solutions.
	* Worst runtime O(2^n), best runtime you usually see O(n)
* [K Difference](kDifference.py)
	* Given array of distinct integers, count the number of pairs of integers with difference k.
	* Runtime is O(n) on average.
* [No Duplicates](no_duplicates.py)
* [Rotate Left](rotLeft.py)
	* Shift each element d units to the left.
* [Sum to K](sum_to_k.py)
	* Given an array of integers (not necessarily distinct), return the number of pairs that sum to k.
	* Average runtime O(n)

## Less Relevant Problems
* [Bone Trousle](bonetrousle.py)
    * Given the values of n, k, and b for trips to the store, determine which boxes Papyrus must purchase during each trip. He purchases exactly b boxes, has k boxes availble at the store where each box contains k sticks, wants n sticks total. Outputs one possible solution.
    * Runtime: O(b)?
* [Counting Valleys](countingValleys.py)
	* From HackerRank
* [Hour Glass Sum](hourGlassSum.py)
	* Return the maximum hourglass sum in a 2D array. An hourglass in A is a subset of values with indices falling in an hourglass pattern.
* [Jumping on Clouds](jumpingOnClouds.py)
	* Return the minimum number of jumps it'll take Emma to jump from her starting position to the last cloud.
* [Minimum Bribes](minimumBribes.py)
* [Sock Merchant](sockMerchant.py)