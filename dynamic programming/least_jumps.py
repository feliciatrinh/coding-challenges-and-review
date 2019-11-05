"""
Input: array of non-negative integers
Output: either the elements you land on or the indices of those elements that get you the least number of jumps

Example
Input: [1, 3, 4, 2, 0, 0, 5]
Output: jumps on elements 1 -> 3 -> 4 -> 5 or indices [0, 1, 2, 6]

Subproblem:
f(i) is the minimum number of jumps it takes to go from the 0th index to the ith index

Recurrence relation: 
f(i) = min {f(i), f(j) + 1} if i <= j + arr[j] for all j < i?
You could have a value filled in for f(i) already from a lower value of j so you need to consider f(i) in the minimum as well.
Can initialize the array with sys.mathsize?

Runtime: O(n^2), there is a linear solution out there though

Notes: can be represented as a DAG where the valid path is the only one with an edge to the last index?
Use one array to keep track of the number of jumps
num_jumps = [0, ...]
Another array to keep track of the actual jump
actual_jump = [-1, 0, ...]

Since we use an array to keep track of the actual jumps as we iterate through the array,
can we only consider j's that are greater than or equal to the last element in actual_jump?

To get the path, you get the value at actual_jump[end] then the value at actual_jump[actual_jump[end]] ...
and build your list backwards.
Example: [-1, 0, 0, 1, 1, 4, 4, 5, 5, 5]
end = 9
so you get actual_jump[9] which is 5
then actual_jump[5] which is 4
then actual_jump[4] which is 1
then actual_jump[1] which is 0
Number of jumps is 4 with path 0 -> 1-> 4 -> 5 -> 9
"""

def least_jumps(arr):
