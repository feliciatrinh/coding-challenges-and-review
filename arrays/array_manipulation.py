"""
Source: Hackerrank
Input: n (size of the array) and queries (2D array of m operations where each query contains three 
       integers: a, b, and k)
Output: Maximum value in array as a long int

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array
elements between two given indices, inclusive. Once all operations have been performed, return the max value in your
array.

Runtime: O(m + n)

Example
Input:
a  b  k
1  2  10
2  3  15
3  4  2
1  6  14
5  6  3

Output: 39

Idea
- each element of arr will represent the difference between the value that should be at this index and the value that
  should be at the previous index
- example: if we have an arr of length 1 where k = 2, arr = [2] b/c we treat the previous element as 0
- example: if we have n = 7, a = 1, b = 5, k = 3 then arr = [3, 0, 0, 0, 0, -3, 0]
  b/c our actual array should look like [3, 3, 3, 3, 3, 0, 0]
"""


def array_manipulation(n, queries):
    arr = [0] * n
    for row in queries:
        # arr is 1-indexed, so we subtract 1
        left = row[0] - 1
        # The value at the right index in arr represents the difference between the element that should be at the right
        # index in our actual array and the last element we added k to.
        right = row[1]
        k = row[2]
        arr[left] += k
        # If you add k to every element in arr then the difference between each element remains the same, otherwise you
        # need to re-calculate the difference.
        if right < len(arr):
            arr[right] -= k

    maximum = 0
    curr_value = 0
    # The current value is the current cumulative sum of the differences.
    for elem in arr:
        curr_value += elem
        if curr_value > maximum: 
            maximum = curr_value
    return maximum


assert array_manipulation(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]]) == 10
assert array_manipulation(7, [[1, 2, 10], [2, 3, 15], [3, 4, 2], [1, 6, 14], [5, 6, 3]]) == 39
