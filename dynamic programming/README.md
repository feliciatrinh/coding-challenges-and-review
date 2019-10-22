# Dynamic Programming

* [Largest Sum](largest_sum.py)
	* Given an array of n integers, find the consecutive indices that give the largest sum.
	* Runtime: 
* [Longest Increasing Subsequence LIS](longest_increasing_subsequence.py)
	* Given an array of integers, return the longest increasing subsequence.
	* Dynamic programming: turns the problem into a DAG. Runtime O(n^2)
* [Edit Distance]
	* Given two strings x and y, find the minimum number of edits needed to transform x into y
	* Runtime O(n^2)

* Notes
	* Define the subproblem; there's an ordering to the subproblems and a (recurrence) relation that shows how to solve the subproblems such that each subproblem only relies on the solution to the smaller ones before it.
	* Define the base case